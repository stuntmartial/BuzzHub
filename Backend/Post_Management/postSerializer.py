from rest_framework.serializers import ModelSerializer
from .models import Content , Like , Comment

class postSerializer(ModelSerializer):

    class Meta:
        model = Content
        fields = [
            'creator',
            'caption',
            'image',   
            'uploaded_time',
            'like_count',
            'comment_count'
        ]

        
class likeSerializer(ModelSerializer):
    
    class Meta:
        model = Like
        fields = [
            'postId',
            'liked_by',
        ]

class commentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'postId',
            'commented_by',
            'comment',
        ]