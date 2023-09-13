from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from user.views import RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),

]