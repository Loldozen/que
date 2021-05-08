from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from user.models import Patient

class PatientAuthenticationBackend(ModelBackend):
    def authenticate(self,request,email=None,password=None):
        try:
            patient = Patient.objects.get(email=email)
            
        except Patient.DoesNotExist:
            return None
        else:
#             if user.check_password(password) and user.is_active:
            if patient.check_password(password):
                return patient

    def get_user(self, user_id):
        try:
            return Patient.objects.get(id=user_id)
        except Patient.DoesNotExist:
            return None