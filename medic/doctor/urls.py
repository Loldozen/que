from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.api_root),
    path('signup/', views.DoctorSignup.as_view(), name='signup'),
]