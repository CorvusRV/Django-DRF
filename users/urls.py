from django.urls import path
from .views import CustomUserAPIView, CustomUserDetailAPIView

app_name = 'users'

urlpatterns = [
    path('users/', CustomUserAPIView.as_view()),
    path('users/<pk>/', CustomUserDetailAPIView.as_view()),
]
