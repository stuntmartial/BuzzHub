from django.db import models
from Profile.models import ProfileModel

class Suggestion(models.Model):
    suggestionId = models.AutoField(primary_key=True)
    profile = models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='profile')
    suggestionString = models.CharField(max_length=500,blank=True)

class IgnoredSuggestions(models.Model):
    ignoredId = models.AutoField(primary_key=True)
    profile = models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='profile_ig')
    ignoredString = models.CharField(max_length=500,blank=True)