from django.contrib import admin
from .models import ProfileModel , ProfilePicModel

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'firstname',
        'lastname',
        'nickname',
        'bio',
        'email',
        'dateofbirth',
        'educationFieldString',
        'educationConcentrationString',
        'educationDegreeString',
        'school',
        'educationType',
        'graduationYear',
        'gender',
        'hometown',
        'locality',
        'languagesString',
        'localeString',
        'employerString',
        'workStartyearString',
        'workEndyearString',
        'workLocationString',
        'workPositionString',
        ]

class ProfilePicModelAdmin(admin.ModelAdmin):
    list_display = [
        'pic_id',
        'profile',
        'profile_pic'
    ]

admin.site.register(ProfileModel,ProfileModelAdmin)
admin.site.register(ProfilePicModel,ProfilePicModelAdmin)


