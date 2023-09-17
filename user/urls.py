from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from user.views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),

]