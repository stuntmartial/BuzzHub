#from Profile.models import ProfileModel
from .models import Relationship
from django.db.models import Q

def getConnectionsList(profile):

    connectionsList = list()

    relnsList = Relationship.objects.filter(
        Q(entity1 = profile) & Q(connection_status = 'Accepted')
    )

    for i in relnsList:
        connectionsList.append(i.entity2)

    relnsList = Relationship.objects.filter(
        Q(entity2 = profile) & Q(connection_status = 'Accepted')
    )

    for i in relnsList:
        connectionsList.append(i.entity1)

    return connectionsList

def getConnectionRequests(profile):
    
    connectionReqList = list()

    relnsList = Relationship.objects.filter(
        Q(entity1 = profile) & Q(connection_status = 'Waiting')
    )

    for i in relnsList:
        connectionReqList.append(i.entity2)

    relnsList = Relationship.objects.filter(
        Q(entity2 = profile) & Q(connection_status = 'Waiting')
    )

    for i in relnsList:
        connectionReqList.append(i.entity1)

    return connectionReqList
