from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from user import urls as user_urls
from category import urls as category_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include(user_urls)),
    path('api/category/', include(category_urls)),

]
