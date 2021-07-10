from django.urls import path
from .views import NewsFeed

urlpatterns = [
    path('getNewsFeedProps/',NewsFeed.as_view()),
]