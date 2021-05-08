from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from doctor.models import Doctor

class DoctorAuthenticationBackend(ModelBackend):
    def authenticate(self,request,email=None,password=None):
        try:
            doctor = Doctor.objects.get(email=email)
            
        except Doctor.DoesNotExist:
            return None
        else:
#             if user.check_password(password) and user.is_active:
            if doctor.check_password(password):
                return doctor

    def get_user(self, user_id):
        try:
            return Doctor.objects.get(id=user_id)
        except Doctor.DoesNotExist:
            return None