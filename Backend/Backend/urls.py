from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from SignUp import views as SignUpViews
from LogIn import views as LogInViews
from Logout import views as LogoutViews
from Profile import views as ProfileViews
from Connection_Management import urls as ConnManagementurls
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView
from Post_Management import urls as PMurls
from NewsFeed import urls as NewsFeedurls
from Recommendation import urls as Recommedationurls
from Profile import urls as Profileupdateurls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Gateway Urls
    path('SignUp/',SignUpViews.SignUp.as_view()),
    path('LogIn/',LogInViews.LogIn.as_view()),
    path('LogOut/',LogoutViews.Logout.as_view()),
    
    #Profile Search and Check Urls
    path('Profile/<req_Profile>/',ProfileViews.ProfilePageStates.as_view()),
    path('Profile/CheckProfile/<target_Profile>/',ProfileViews.CheckProfile.as_view()),
    
    #Profile update urls
    path('update/',include(Profileupdateurls)),
    
    #JWT urls
    path('getToken/',TokenObtainPairView.as_view(),name='getToken'),
    path('refreshToken/',TokenRefreshView.as_view(),name='refreshToken'),
    path('verifyToken/',TokenVerifyView.as_view(),name='verifyToken'),

    #Connection Management Urls
    path('',include(ConnManagementurls)),

    #Post Management Urls
    path('Post/',include(PMurls)),

    #Newsfeed Urls
    path('',include(NewsFeedurls)),

    #Recommendation Urls
    path('',include(Recommedationurls)),
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    