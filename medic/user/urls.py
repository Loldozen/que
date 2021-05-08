from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.api_root),
    path('signup/', views.Signup.as_view(), name='signup'),
    #path('login/', views.Login.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='obtain_token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
]