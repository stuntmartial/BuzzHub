from Profile.models import ProfilePicModel
from django.contrib.auth.models import User
from Recommendation.models import Suggestion,IgnoredSuggestions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.db.models import Q
from Profile.views import CreateProfile


def chkExistanceUsername(username):

    querySet = User.objects.filter(
        Q(username = username)
    )

    if len(list(querySet)) == 0:
        return False
    else:
        return True

def chkExistanceEmail(email):

    querySet = User.objects.filter(
        Q(email = email)
    )

    if len(list(querySet)) == 0:
        return False
    else:
        return True

class SignUp(APIView):

    #Registers a new user

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self,request,format=None):

        
        request_data = request.data
        username = request_data.get('Username',None)
        firstname = request.data.get('Firstname',None)
        lastname = request.data.get('Lastname',None)
        gender = request.data.get('Gender',None)
        email = request_data.get('Email',None)
        password = request_data.get('Password',None)
        
        duplicateUsernameFlag = chkExistanceUsername(username)
        duplicateEmailFlag = chkExistanceEmail(email)

        if duplicateUsernameFlag:

            data = {
            'msg' : 'Please try with different Username',
            }

            return Response(data = data , status = HTTP_200_OK)

        if duplicateEmailFlag:

            data = {
            'msg' : 'Please try with different Email',
            }

            return Response(data = data , status = HTTP_200_OK)

        user = User(
            username = username,
            email = email,
            password = password
            )

        user.set_password(password)
        user.save()
        
        Profile_obj = CreateProfile(
            user_obj = user,
            email = email,
            firstname=firstname,
            lastname=lastname,
            gender=gender
        )

        ProfilePicModel(
            profile = Profile_obj
        ).save()
        
        Suggestion(
            profile = Profile_obj
        ).save()

        IgnoredSuggestions(
            profile = Profile_obj
        ).save()

        data = {
            'msg' : 'Data Created',
            'username' : username}

        return Response(data = data , status = HTTP_201_CREATED)
