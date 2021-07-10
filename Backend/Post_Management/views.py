from .models import Content
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE
from Profile.models import ProfileModel
from .postSerializer import postSerializer , likeSerializer , commentSerializer
from datetime import datetime
from .models import Like
from django.db.models import Q

class CreatePost(APIView):

    #creates a post

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser , FormParser]

    def post(self,request,format=None):

        creator = request.user.username
        caption = request.data.get('caption',None)
        image = request.data.get('image',None)
        
        data = {
            'creator' : creator,
            'caption' : caption,  
            'image' : image,
            'shared_by' : creator,
            'uploaded_time' : datetime.now()
        }

        contentIns = postSerializer(data = data)

        if contentIns.is_valid():
            contentIns.save()

            data = {
                'msg' : 'Post Created'
            }

            return Response(data = data , status = HTTP_201_CREATED)

        else:
            data = {
                'msg' : 'Wrong Input'
            }

            return Response(data = data , status = HTTP_406_NOT_ACCEPTABLE)
        

class LikePost(APIView):

    #Add or Undo like to or from a post

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        liked_by = request.user
        liked_by = ProfileModel.objects.get(user = liked_by)
        liked_flag = request.data.get('liked_flag')
        post_id = request.data.get('post_id')
        
        if liked_flag:
            data = {
                'postId' : post_id,
                'liked_by' : liked_by
            }

            likeIns = likeSerializer(data = data)
            
            if likeIns.is_valid():
                likeIns.save()
            
            content = Content.objects.get(postId = post_id)
            content.like_count += 1
            content.save()

            data = {
                'msg' : 'Liked'
            }

        else:
            likeIns = Like.objects.filter(
                Q(liked_by = liked_by) & Q(postId = post_id)
            )

            likeIns.delete()

            content = Content.objects.get(postId = post_id)
            content.like_count -= 1
            content.save()

            data = {
                'msg' : 'Like Revoked'
            }

        return Response(data = data , status = HTTP_200_OK)

class CommentPost(APIView):

    #Add Comment to a post

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        print(request.data)
        
        commented_by = request.user
        commented_by = ProfileModel.objects.get(user = commented_by)
        comment = request.data.get('comment')
        post_id = request.data.get('post_id')

        contentIns = Content.objects.get(postId=post_id)

        data = {
            'postId' : post_id,
            'commented_by' : commented_by,
            'comment' : comment
        }

        commentIns = commentSerializer(data = data)
        
        if commentIns.is_valid():
            commentIns.save()

        contentIns.comment_count +=1
        contentIns.save()
        
        data = {
            'msg' : 'Commented'
        }

        return Response(data = data , status = HTTP_200_OK)
