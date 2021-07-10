import pandas as pd
import tensorflow as tf
from tensorflow import keras
import tensorflow_addons as tfa
from DeepLinker import DEEPLINKER

#Defining constants and model hyper-parameters
NODES = 0
NUM_FEATS = 0
ADJ_MATRIX = list()
ZEROS_ADJ_MATRIX=0
ONES_ADJ_MATRIX=0
RATIO = 0
INTERMEDIATE_DIMS = 100
OUT_DIMS = 50
LEARNING_RATE = 5e-3
EPOCH = 1800

#Generating dataframes
node_feats_df=pd.read_csv('Datasets/Node_feats_Network1.csv')
edge_list_df=pd.read_csv('Datasets/Edges.csv')

#Generating Input Node Embedding Matrix
node_feats=[]
NUM_FEATS = len(node_feats_df.columns) - 1
NODES = len(node_feats_df)

for i in range(len(node_feats_df)):
    feat=[]
    for j in range(1,NUM_FEATS+1):
        feat.append(node_feats_df.iloc[i][j])
    node_feats.append(feat)

node_feats=tf.convert_to_tensor(node_feats,dtype=tf.float32)

#Extracting edges from edge_list_df dataframe
edge_list=[]
for i in range(len(edge_list_df)):
    src=edge_list_df.iloc[i][0]
    trg=edge_list_df.iloc[i][1]
    edge_list.append((src,trg))

#Initializing Adjacency Matrix
for i in range(NODES):
    ADJ_MATRIX.append([0]*NODES)

#Generating Adjacency Matrix from EdgeList representation of graph
for edge in edge_list:
    src=edge[0]
    trg=edge[1]
    ADJ_MATRIX[src][trg]=1
    ADJ_MATRIX[trg][src]=1

#Adding self-loops
for i in range(NODES):
    for j in range(NODES):
        if i==j:
            ADJ_MATRIX[i][j]=1

#Ratio of number of zeros and ones in Adjacency Matrix
for i in range(NODES):
    for j in range(NODES):
        if ADJ_MATRIX[i][j]==0:
            ZEROS_ADJ_MATRIX+=1
        else:
            ONES_ADJ_MATRIX+=1

RATIO = ONES_ADJ_MATRIX / ZEROS_ADJ_MATRIX

ADJ_MATRIX=tf.convert_to_tensor(ADJ_MATRIX,dtype=tf.float32)

#Creating DEEPLINKER instance
DEEPLINKER_obj=DEEPLINKER(intermediate_dims=INTERMEDIATE_DIMS,out_dims=OUT_DIMS)

#Defining loss function and optimizer
loss_fn = tfa.losses.focal_loss.SigmoidFocalCrossEntropy(alpha=RATIO,gamma=2)
optim_fn = keras.optimizers.Adam(learning_rate=5e-3)

#Reshaping Adjacency matrix into ADJ_MATRIX_ for calculating loss during training
ADJ_MATRIX_ = tf.reshape(ADJ_MATRIX,shape=(NODES*NODES,1))

#Training Loop
for epoch in range(EPOCH):
    
    with tf.GradientTape() as tape:
        y_hat = DEEPLINKER_obj( [node_feats,ADJ_MATRIX] )
        y_hat = tf.reshape(y_hat,shape=(NODES*NODES,1))
        loss = loss_fn(ADJ_MATRIX_,y_hat)
        loss = tf.reduce_sum(loss)
        
    print('Epoch ---> ',epoch,' Loss ---> ',loss.numpy())

    grads = tape.gradient(loss, DEEPLINKER_obj.trainable_variables)
    optim_fn.apply_gradients(zip(grads, DEEPLINKER_obj.trainable_variables))

#Saving the model
keras.models.save_model(DEEPLINKER_obj,"../DEEPLINKER_MOD",overwrite=True)