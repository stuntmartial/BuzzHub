from Connection_Management.models import Relationship
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from Profile.models import ProfileModel,ProfilePicModel
from Profile.dpSerializer import dpSerializer
from Connection_Management.utility import getConnectionsList
from .utility import getPosts
from Recommendation.models import Suggestion,IgnoredSuggestions
from django.contrib.auth.models import User
from django.db.models import Q



class NewsFeed(APIView):

    #Generates NewsFeed for a specific profile
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        
        user = request.user
        profile = ProfileModel.objects.get(user = user)
        profilepic = list(ProfilePicModel.objects.filter(profile=profile))[0]
        profilepic = dpSerializer(profilepic).data

        connections = list(getConnectionsList(profile))
        connections.append(profile)
        
        posts_dict = getPosts(connections,profile)
        posts_dict.sort(key = lambda x : x['uploaded_time'] , reverse = True)
        
        postCreatorImgs = list()
        for post in posts_dict:
            creator = post['creator']
            creatorUser = list(User.objects.filter(username=creator))[0]
            creator_prof = ProfileModel.objects.get(user=creatorUser)
            creatorImg = list(ProfilePicModel.objects.filter(profile=creator_prof))[0]
            creatorImg = dpSerializer(creatorImg).data
            postCreatorImgs.append(creatorImg)
    
        suggestionObj= list(Suggestion.objects.filter(profile=profile))[0]
        suggestionString = suggestionObj.suggestionString
        suggestionList = [sugg for sugg in suggestionString.split('#')]

        ignoredList = list(IgnoredSuggestions.objects.filter(profile=profile))[0].ignoredString
        
        suggestionListRefined = list()
        for sugg in suggestionList:
            print(sugg)
            if sugg not in ignoredList:
                suggestionListRefined.append(sugg)

        if suggestionListRefined[0]=='':
            suggestionListRefined.pop(0)
                    
        if len(suggestionListRefined)==0:
            data = {
            'msg' : 'Ok',
            'Profile' : profile.user.username,
            'Profile_pic' : profilepic,
            'Posts' : posts_dict,
            'Suggestions' : suggestionListRefined,
            'postCreatorImgs' : postCreatorImgs
            }

            return Response( data = data , status = HTTP_200_OK )


        index = 0
        while index < len(suggestionListRefined):
            sugg = suggestionListRefined[index]
            suggUser = list(User.objects.filter(username=sugg))[0]
            suggProfile = ProfileModel.objects.get(user=suggUser)

            suggFlag = list(Relationship.objects.filter(
                Q(entity1 = profile) & Q(entity2 =suggProfile)
            ))

            if len(suggFlag)>0:
                suggestionListRefined.pop(index)
                continue

            suggFlag = list(Relationship.objects.filter(
                Q(entity2 = profile) & Q(entity1 =suggProfile)
            ))

            if len(suggFlag)>0:
                suggestionListRefined.pop(index)
                continue

            index += 1

        if len(suggestionListRefined)>=7:
            suggestionListRefined = suggestionListRefined[:7]
        
        data = {
            'msg' : 'Ok',
            'Profile' : profile.user.username,
            'Profile_pic' : profilepic,
            'Posts' : posts_dict,
            'Suggestions' : suggestionListRefined,
            'postCreatorImgs' : postCreatorImgs
        }

        return Response( data = data , status = HTTP_200_OK )
