from category.views import UserCategoryAPI

from django.urls import path

urlpatterns = [
    path('user_category/',UserCategoryAPI.as_view(), name="user-category" ),
]