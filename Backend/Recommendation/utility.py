from django.db.models import Q
import tensorflow as tf
from tensorflow import keras
from Connection_Management.models import Relationship
from Connection_Management.utility import getConnectionsList
from .models import Suggestion
from .NodeEmbeddingGenerator import generateNodeEmbedding

RECOMMENDATION_THRESHOLD = 0.8
strSEPARATOR = "#"
MAX_NODES = 348
FEATS = 224

def createHash(edgeList):

    edgelist = list(edgeList)
    user_index_hash = dict()
    index_user_hash = dict()
    zeroIndexedcount = -1

    for reln in edgelist:
        entity1 = reln.entity1
        entity2 = reln.entity2

        if entity1 not in user_index_hash.keys():
            zeroIndexedcount += 1
            user_index_hash [entity1] = zeroIndexedcount
            index_user_hash [zeroIndexedcount] = entity1

        if entity2 not in user_index_hash.keys():
            zeroIndexedcount += 1
            user_index_hash [entity2] = zeroIndexedcount
            index_user_hash [zeroIndexedcount] = entity2

    return zeroIndexedcount , user_index_hash , index_user_hash

def getoneIndices(connections,user_index_hash):
    
    oneIndices = list()
    for con in connections:
        index = user_index_hash[con]
        oneIndices.append(index)

    return oneIndices

def createAdJMATRIX(zeroIndexedcount , user_index_hash , index_user_hash):
    global MAX_NODES
    ADJ_MATRIX = list()
    for _ in range(MAX_NODES):
        ADJ_MATRIX.append([0] * (MAX_NODES))

    for index in range(zeroIndexedcount + 1):
        profile = index_user_hash[index]
        connections = getConnectionsList(profile)
        oneIndices = getoneIndices(connections,user_index_hash)
        for j in range(len(oneIndices)):
            ADJ_MATRIX[index][j] = 1

        ADJ_MATRIX[index][index] = 1
    return ADJ_MATRIX

def getNodeEmbeddings(user_index_hash):
    global MAX_NODES,FEATS

    profiles = list(user_index_hash.keys())

    Node_Embeddings = list()
    
    for profile in profiles:
        emb = generateNodeEmbedding(profile)
        Node_Embeddings.append([i for i in emb])

    for _ in range(MAX_NODES-len(profiles)):
        Node_Embeddings.append([0]*FEATS)

    return Node_Embeddings

def setSuggestions(ADJ_MATRIX , opADJMATRIX , index_user_hash , zeroIndexedcount):
        global RECOMMENDATION_THRESHOLD , strSEPARATOR

        for index in range(zeroIndexedcount + 1):
            
            suggestionString = ''
            for j in range(zeroIndexedcount + 1):
                if ADJ_MATRIX[index][j] == 0 and opADJMATRIX[index][j] >= RECOMMENDATION_THRESHOLD:
                    profile = index_user_hash[j]
                    suggestionString += profile.user.username + strSEPARATOR
            suggestionString = suggestionString[:-1]

            profile = index_user_hash[index]
            suggestionInstance = list(Suggestion.objects.filter(
                Q(profile = profile)
            ))[0]

            suggestionInstance.suggestionString = suggestionString
            suggestionInstance.save()

def runForwardProp():

    edgeList = Relationship.objects.filter(
        Q(connection_status = 'Accepted')
    )
    
    zeroIndexedcount , user_index_hash , index_user_hash = createHash(edgeList)
    
    ADJ_MATRIX = createAdJMATRIX(zeroIndexedcount , user_index_hash , index_user_hash)
    NODE_EMBEDDINGS = getNodeEmbeddings(user_index_hash)
    
    DEEPLINKER = keras.models.load_model('Recommendation/DEEPLINKER_MOD')
    
    ADJ_MATRIX_ = tf.convert_to_tensor(ADJ_MATRIX , dtype=tf.float32)
    NODE_EMBEDDINGS = tf.convert_to_tensor(NODE_EMBEDDINGS , dtype=tf.float32)
    
    print('FORWARD PROPAGATION >>>>>>>>>>>>>>>>')
    
    opADJMATRIX = DEEPLINKER([ NODE_EMBEDDINGS , ADJ_MATRIX_])
    
    print('FORWARD PROPAGATION ENDS')
    
    opADJMATRIX = opADJMATRIX.numpy().tolist()
    
    setSuggestions(ADJ_MATRIX , opADJMATRIX , index_user_hash , zeroIndexedcount)
    