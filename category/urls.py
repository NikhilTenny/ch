from category.views import UserCategoryAPI

from django.urls import path

urlpatterns = [
    path('user_category/create',UserCategoryAPI.as_view(), name="create-user-category" ),
    path('user_category/list',UserCategoryAPI.as_view(), name="list-user-category" ),
]