from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Relationship
from Profile.models import ProfileModel


class SendConnectionRequest(APIView):

    #Send Connection Request to a profile

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        sender = ProfileModel.objects.get(user = request.user)
        receiver = request.data.get('receiver',None)
        receiver = list(User.objects.filter(Q(username=receiver)))[0]
        
        receiver = ProfileModel.objects.get(user = receiver)
        
        reln_obj = Relationship(
            entity1 = sender,
            entity2 = receiver,
            sender = sender,
        )
        
        reln_obj.save()

        data = {
            'msg' : 'Connection Request Sent'
        }

        return Response(data = data , status = HTTP_200_OK)

class AcceptConnectionRequest(APIView):

    #Accept Connection Request from a profile

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):

        receiver = ProfileModel.objects.get(user = request.user)
        sender = request.data.get('sender')
        sender = list(User.objects.filter(Q(username=sender)))[0]
        sender = ProfileModel.objects.get(user = sender)

        reln_obj = Relationship.objects.filter(
            Q(entity1 = sender) &
            Q(entity2 = receiver) &
            Q(connection_status = 'Waiting')
        )[0]

        reln_obj.connection_status = 'Accepted'
        reln_obj.save()

        data = {
            'msg' : 'Conection Request Accepted'
        }

        return Response(data = data , status = HTTP_200_OK)

class RejectConnectionRequest(APIView):

    #Reject Connection Request from a profile

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):

        receiver = ProfileModel.objects.get(user = request.user)
        sender = request.data.get('sender')
        sender = list(User.objects.filter(Q(username=sender)))[0]
        sender = ProfileModel.objects.get(user = sender)

        reln_obj = Relationship.objects.filter(
            Q(entity1 = sender) &
            Q(entity2 = receiver) &
            Q(connection_status = 'Waiting')
        )[0]

        reln_obj.connection_status = 'Rejected'
        reln_obj.save()

        data = {
            'msg' : 'Conection Request Rejected'
        }

        return Response(data = data , status = HTTP_200_OK)

class DeleteConnection(APIView):

    #Delete any Connection
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        del_req_initializer = ProfileModel.objects.get(user = request.user)
        other_end_user = request.data.get('other_end_user',None)
        other_end_user = list(User.objects.filter(Q(username=other_end_user)))[0]
        other_end_user = ProfileModel.objects.get(user = other_end_user)


        querySet = Relationship.objects.filter(
            Q(entity1 = del_req_initializer) & Q(entity2 = other_end_user)
        )
        if len(list(querySet)) == 0:
            querySet = Relationship.objects.filter(
            Q(entity1 = other_end_user) & Q(entity2 = del_req_initializer)
        )

        reln_obj = list(querySet)[0]
        reln_obj.delete()

        data = {
            'msg' : 'Deleted Connection'
        }

        return Response(data = data , status = HTTP_200_OK)
