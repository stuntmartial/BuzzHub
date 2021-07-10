from django.db import models
from Profile.models import ProfileModel
from datetime import datetime

def upload_to(instance,filename):
    return 'posts/Img_{creator}_{filename}'.format(creator = instance.creator,filename=filename)

class Content(models.Model):
    postId=models.AutoField(primary_key=True)
    creator=models.CharField(max_length=200)
    caption=models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to = upload_to,default = 'posts/default.jpg',blank=True)
    like_count=models.IntegerField(default=0)
    comment_count=models.IntegerField(default=0)
    uploaded_time=models.DateTimeField(default=datetime.now())

class Like(models.Model):
    likeId=models.AutoField(primary_key=True)
    postId=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='LikepostId')
    liked_by=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='liked_by')

class Comment(models.Model):
    commentId=models.AutoField(primary_key=True)
    postId=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='CommentpostId')
    commented_by=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='commented_by')
    comment=models.CharField(max_length=100)

class Share(models.Model):
    shareId=models.AutoField(primary_key=True)
    postId=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='SharepostId')
    shared_by=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='shared_by')
