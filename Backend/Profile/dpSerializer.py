from rest_framework.serializers import ModelSerializer
from .models import ProfilePicModel

class dpSerializer(ModelSerializer):

    class Meta:
        model = ProfilePicModel
        fields = [
            'profile',
            'profile_pic'
        ]