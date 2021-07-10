from django.urls import path
from .views import *

urlpatterns = [
    path('sendCon/',SendConnectionRequest.as_view()),
    path('acceptCon/',AcceptConnectionRequest.as_view()),
    path('rejectCon/',RejectConnectionRequest.as_view()),
    path('delCon/',DeleteConnection.as_view()),   
]