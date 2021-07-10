from django.contrib.auth import authenticate , login
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class LogIn(APIView):


    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self,request,format=None):
        
        request_data = request.data
        username = request_data.get('Username',None)
        password = request_data.get('Password',None)
        
        user_existance_flag = authenticate(username=username,password=password)

        if user_existance_flag is not None:
            
            login(
                request,
                user_existance_flag
                )
            
            data = {
                'msg' : 'Logged In',
                }

            return Response(data = data , status = HTTP_200_OK)
        
        else:

            data = {
                'msg' : 'Please LogIn with correct credentials'
            }
            return Response(data = data , status = HTTP_200_OK)