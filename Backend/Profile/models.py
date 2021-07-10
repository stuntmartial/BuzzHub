from django.db import models
from django.contrib.auth.models import User
from datetime import date

def upload_to(instance,filename):
    return 'profile_pics/Img_{creator}_{filename}'.format(creator = instance.profile.user.username,filename=filename) #  ----> see this

class ProfileModel(models.Model):
    
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE,primary_key=True)
    firstname=models.CharField(max_length=30,default='FirstName')
    lastname=models.CharField(max_length=30,default='LastName')
    nickname=models.CharField(max_length=30,default='NickName')
    bio=models.TextField(max_length=100,default='//')
    email=models.EmailField(max_length=100,default='')
    
    dateofbirth=models.CharField(max_length = 20,default='1/1/1900')
    educationFieldString=models.CharField(max_length=100,default='//')
    educationConcentrationString=models.CharField(max_length=100,default='//')
    educationDegreeString=models.CharField(max_length=100,default='//')
    school=models.CharField(max_length=100,default='//')
    educationType=models.CharField(max_length=50,default='//')
    graduationYear=models.CharField(max_length = 10,default='1900')
    gender=models.CharField(max_length=10,default='/')
    hometown=models.CharField(max_length=50,default='//')
    locality=models.CharField(max_length=50,default='//')
    languagesString=models.CharField(max_length=100,default='//')
    localeString=models.CharField(max_length=100,default='//')
    employerString=models.CharField(max_length=100,default='//')
    workStartyearString=models.CharField(max_length=100,default='//')
    workEndyearString=models.CharField(max_length=100,default='//')
    workLocationString=models.CharField(max_length=100,default='//')
    workPositionString=models.CharField(max_length=100,default='//')

class ProfilePicModel(models.Model):
    pic_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='profile_profile_pic')
    profile_pic=models.ImageField(upload_to=upload_to,default='profile_pics/default.jpg',blank=True)
    



