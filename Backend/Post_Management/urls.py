from django.urls import path
from .views import CreatePost , LikePost , CommentPost

urlpatterns = [
    path('createPost/',CreatePost.as_view()),
    path('likePost/',LikePost.as_view()),
    path('commentPost/',CommentPost.as_view()),
]