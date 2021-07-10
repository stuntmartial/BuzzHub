from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from Profile.models import ProfileModel
from .models import IgnoredSuggestions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User

class IgnoreView(APIView):


    #Ignores suggestion to ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        
        user = request.user
        profile = ProfileModel.objects.get(user=user)
        ignoredProfile = request.data.get('ignoredProfile',None)

        if ignoredProfile==None:
            data={
                'msg' : 'No profile received'
            }

            return Response(data=data , status = HTTP_200_OK)

        ignoredUser = list(User.objects.filter(username=ignoredProfile))
        
        if len(ignoredUser) == 0:
            data={
                'msg' : 'No such profile found'
            }
            return Response(data=data , status=HTTP_200_OK)

        ignoredUser = ignoredUser[0]
        
        ignoredObj = list(IgnoredSuggestions.objects.filter(profile=profile))[0]
        ignoredObj.ignoredString = "#" + ignoredUser.username

        ignoredObj.save()

        data={
            'msg' : 'OK'
        }

        return Response(data=data , status=HTTP_200_OK)        

