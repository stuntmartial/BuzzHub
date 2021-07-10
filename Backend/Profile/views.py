from django.db.models import Q
from rest_framework.response import Response
from .models import ProfileModel, ProfilePicModel
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from Post_Management.utility import getPosts
from django.contrib.auth.models import User
from Connection_Management.models import Relationship
from Connection_Management.utility import getConnectionsList , getConnectionRequests
from rest_framework.parsers import MultiPartParser , FormParser
from datetime import datetime
from .dpSerializer import dpSerializer

def CreateProfile(user_obj = None , email = None , firstname = None , lastname = None , gender = None):

    #Creates a user profile
        
    if user_obj == None or email == None:
        return False

    Profile_obj = ProfileModel(
        user = user_obj,
        email = email,
        firstname = firstname,
        lastname = lastname,
        gender=gender
    )

    Profile_obj.save()
    return Profile_obj

class ProfilePageStates(APIView):

    #Generates the Profile page
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,req_Profile,format=None):
        
        user = request.user.username
        req_Profileobj = list(User.objects.filter(username=req_Profile))
        
        if len(req_Profileobj)==0:
            data={
                'msg' : 'No such profile'
            }

            return Response(data = data , status=HTTP_200_OK)

        req_Profileobj = ProfileModel.objects.get(user=req_Profileobj[0])
        profileObj = ProfileModel.objects.get(user=request.user)

        connections_list = [conn.user.username for conn in getConnectionsList(req_Profileobj)]
        connection_reqs = [conn.user.username for conn in getConnectionRequests(req_Profileobj)]
        
        picObj = list(ProfilePicModel.objects.filter(profile=req_Profileobj))[0]
        picObj = dpSerializer(picObj).data
        
        if user == req_Profile:    
            posts = getPosts(profileObj,profileObj)
            posts.sort(key = lambda x : x['uploaded_time'] , reverse = True)
            
            postCreatorImgs = list()
            for post in posts:
                creator = post['creator']
                creatorUser = list(User.objects.filter(username=creator))[0]
                creator_prof = ProfileModel.objects.get(user=creatorUser)
                creatorImg = list(ProfilePicModel.objects.filter(profile=creator_prof))[0]
                creatorImg = dpSerializer(creatorImg).data
                postCreatorImgs.append(creatorImg)

            data = {
                'MyProfile' : True,
                'Username' : req_Profile,
                'picObj' : picObj,
                'bio' : req_Profileobj.bio,
                'Connections' : connections_list,
                'Friend_Requests' : connection_reqs,
                'AddFriendFlag' : False,
                'ConnectionReqFlag' : False,
                'EditFlag' : True,
                'posts' : list(posts),
                'postCreatorImgs' : postCreatorImgs 
                }

        else:
            if len( list(Relationship.objects.filter(
                Q(entity1=profileObj) & Q(entity2=req_Profileobj) & Q(connection_status='Accepted')
            )))==0 and len( list(Relationship.objects.filter(
                Q(entity1=req_Profileobj) & Q(entity2=profileObj) & Q(connection_status='Accepted')
            )))==0:

                AddFriendFlag = True
            else:
                AddFriendFlag = False
                
            if len(list(Relationship.objects.filter(
                Q(entity1=profileObj) & Q(entity2=req_Profileobj) & Q(connection_status='Waiting')
                )))==1:
                AddFriendFlag=False
                ConnectionReqFlag = True
            else:
                ConnectionReqFlag = False

            posts = getPosts(req_Profileobj ,profileObj)
            posts.sort(key = lambda x : x['uploaded_time'] , reverse = True)

            postCreatorImgs = list()
            for post in posts:
                creator = post['creator']
                creatorUser = list(User.objects.filter(username=creator))[0]
                creator_prof = ProfileModel.objects.get(user=creatorUser)
                creatorImg = list(ProfilePicModel.objects.filter(profile=creator_prof))[0]
                creatorImg = dpSerializer(creatorImg).data
                postCreatorImgs.append(creatorImg)

            data = {
                'MyProfile' : False,
                'Profile_obj' : req_Profile,
                'Username' : req_Profile,
                'picObj' : picObj,
                'bio' : req_Profileobj.bio,
                'Connections' : connections_list,
                'Friend_Requests' : [],
                'AddFriendFlag' : AddFriendFlag,
                'ConnectionReqFlag' : ConnectionReqFlag,
                'EditFlag' : False,
                'posts' : posts,
                'postCreatorImgs' : postCreatorImgs
                }

            
        return Response(data = data , status = HTTP_200_OK)
        
class CheckProfile(APIView):

    #Checks existance of a specific profile

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,target_Profile,format=None):

        req_user_list = list(User.objects.filter(username=target_Profile))
        
        if len(req_user_list) == 0:
            profileExistance = False
        elif len(req_user_list) == 1:
            profileExistance = True
        
        data = {
            'profileExistance' : profileExistance 
        }

        return Response(data = data , status = HTTP_200_OK)

class AddLang(APIView):

    #Add language to ProfileModel instance
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        lang = request.data.get('lang',None)

        if profileObj.languagesString == "//":
            profileObj.languagesString = lang
        else:
            profileObj.languagesString = profileObj.languagesString + "#" + lang
        
        profileObj.save()

        return Response(data = {'msg':'Bio Updated'} , status=HTTP_200_OK)


class EditBio(APIView):

    #Edit Bio of ProfileModel Instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        bio = request.data.get('bio',None)

        profileObj.bio = bio
        profileObj.save()

        return Response(data = {'msg':'Bio Updated'} , status=HTTP_200_OK)


class EditProfilePic(APIView):

    #Edit Profile Picture of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser , FormParser]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        profile_pic = request.data.get('profile_pic',None)

        picObj = {
            'profile' : profileObj,
            'profile_pic' : profile_pic
        }

        profilepicIns = dpSerializer(data=picObj)
        
        if profilepicIns.is_valid():
            list(ProfilePicModel.objects.filter(profile=profileObj))[0].delete()

            profilepicIns.save()

        return Response(data = {'msg':'Profile_Pic Updated'} , status=HTTP_200_OK)


class EditBday(APIView):

    #Edit birthday of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        bday = request.data.get('bday',None)
        
        profileObj.dateofbirth = bday
        profileObj.save()
        return Response(data = {'msg':'Birthday Updated'} , status=HTTP_200_OK)


class AddEducation(APIView):

    #Add Education to ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)

        educationField = request.data.get('educationField',None)
        educationConcentration = request.data.get('educationConcentration',None)
        educationDegree = request.data.get('educationDegree',None)

        if profileObj.educationFieldString=="//":
            profileObj.educationFieldString = educationField
        else:
            profileObj.educationFieldString = profileObj.educationFieldString + "#" + educationField

        if profileObj.educationConcentrationString=="//":
            profileObj.educationConcentrationString = educationConcentration
        else:
            profileObj.educationConcentrationString = profileObj.educationConcentrationString +"#" + educationConcentration
    
        if profileObj.educationDegreeString=="//":
            profileObj.educationDegreeString = educationDegree
        else:
            profileObj.educationDegreeString = profileObj.educationDegreeString + "#" + educationDegree

        profileObj.save()
        return Response(data={'msg':'Education Added'} , status=HTTP_200_OK)

class EditSchool(APIView): 

    #Edit School of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        school = request.data.get('school',None)
        profileObj.school = school
        profileObj.save()

        return Response(data = {'msg':'School Updated'} , status=HTTP_200_OK)

class EditEduType(APIView): 

    #Edit Education Type of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        educationType = request.data.get('educationType',None)

        profileObj.educationType = educationType
        profileObj.save()

        return Response(data = {'msg':'Education Type Updated'} , status=HTTP_200_OK)

class EditGradYear(APIView): 

    #Edit Graduation Year of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        graduationYear = request.data.get('gradYear',None)

        profileObj.graduationYear = graduationYear
        profileObj.save()

        return Response(data = {'msg':'Graduation Year Updated'} , status=HTTP_200_OK)

class EditResidence(APIView): 

    #Edit Residence of ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        hometown = request.data.get('hometown',None)
        locality = request.data.get('locality',None)
        
        profileObj.hometown = hometown
        profileObj.locality = locality
        profileObj.save()

        return Response(data = {'msg':'hometown Updated'} , status=HTTP_200_OK)

class AddLocale(APIView):

    #Add Locale to ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        locale = request.data.get('locale',None)

        if profileObj.localeString == "//":
            profileObj.localeString=locale
        else:
            profileObj.localeString = profileObj.localeString + "#" + locale

        profileObj.save()
        return Response(data={'msg':'Locale Added'} , status=HTTP_200_OK)

class AddWork(APIView):

    #Add work attributes to ProfileModel instance

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        user = request.user
        profileObj = ProfileModel.objects.get(user=user)
        employer = request.data.get('employer',None)
        workStartyear = request.data.get('workStartyear',None)
        workEndyear = request.data.get('workEndyear',None)
        workLocation = request.data.get('workLocation',None)
        workPosition = request.data.get('workPosition',None)

        if profileObj.employerString=="//":
            profileObj.employerString = employer
        else:
            profileObj.employerString = profileObj.employerString + "#" + employer
    
        if profileObj.workStartyearString=="//":
            profileObj.workStartyearString = workStartyear
        else:
            profileObj.workStartyearString = profileObj.workStartyearString + "#" + workStartyear

        if profileObj.workEndyearString=="//":
            profileObj.workEndyearString = workEndyear
        else:
            profileObj.workEndyearString = profileObj.workEndyearString + "#" + workEndyear

        if profileObj.workLocationString=="//":
            profileObj.workLocationString = workLocation
        else:
            profileObj.workLocationString = profileObj.workLocationString + "#" + workLocation

        if profileObj.workPositionString=="//":
            profileObj.workPositionString = workPosition
        else:
            profileObj.workPositionString = profileObj.workPositionString + "#" + workPosition

        profileObj.save()

        return Response(data={'msg':'Work Added'} , status=HTTP_200_OK)