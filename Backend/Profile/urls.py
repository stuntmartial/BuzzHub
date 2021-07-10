from django.urls import path
from .views import AddLocale, AddWork,EditBio,EditProfilePic,EditBday,AddEducation,EditSchool,EditEduType,EditGradYear,EditResidence,AddLocale,AddWork,AddLang

urlpatterns = [
    path('bio/',EditBio.as_view()),
    path('profile_pic/',EditProfilePic.as_view()),
    path('bday/',EditBday.as_view()),
    path('education/',AddEducation.as_view()),
    path('school/',EditSchool.as_view()),
    path('edutype/',EditEduType.as_view()),
    path('gradyear/',EditGradYear.as_view()),
    path('residence/',EditResidence.as_view()),
    path('locale/',AddLocale.as_view()),
    path('work/',AddWork.as_view()),
    path('lang/',AddLang.as_view())
]