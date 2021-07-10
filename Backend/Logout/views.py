from django.contrib import auth
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class Logout(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        
        logout(request)
        
        data = {
            'msg' : 'Logged Out'
        }
        return Response(data = data , status=HTTP_200_OK)