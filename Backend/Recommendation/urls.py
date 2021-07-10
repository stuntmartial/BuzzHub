from django.urls import path
from .views import IgnoreView

urlpatterns = [
    path('Ignore/',IgnoreView.as_view()),
]