from django.db import models
from Profile.models import ProfileModel

stat=('Waiting','Accepted','Rejected')

class Relationship(models.Model):
    entity1=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='entity1')
    entity2=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='entity2')
    sender=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='sender')
    connection_status=models.CharField(max_length=15,default=stat[0])

