from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from jsonfield import JSONField
from django.contrib.auth import get_user_model

from user.models import CustomUser
from user.managers import CustomUserManager

User = get_user_model()
# Create your models here.
class Doctor(User):
    
    
    """LANGUAGES = (
        ('English','English'),
        ('Yoruba','Yoruba'),
        ('Igbo','Igbo'),
        ('Hausa','Hausa'),
        ('Fulfulde','Fulfulde'),
        ('Tiv','Tiv'),
        ('Nupe','Nupe'),
        ('Kanuri','Kanuri'),
        ('Ibibio','Ibibio'),
        ('French','French'),
        ('Spanish','Spanish'),
        ('Chinese','Chinese'),
    )"""
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    mdcn = models.IntegerField(_('MDCN Number'))
    specialization = models.CharField(_('Specialization'), max_length=50)
    language = models.JSONField(null=True, blank=True)
    agreement = models.BooleanField(_('terms and conditions'), default=False)
    verified = models.BooleanField( default=False)
    objects = CustomUserManager()
    #objects = models.Manager()

    #USERNAME_FIELD = 'mdcn'

    #class Meta:
        #unique_together = (('mdcn'),)
        

    @property
    def get_mdcn(self):
        return 'The MDCN of %s is %s' %(self.name, self.mdcn)
    def save(self, *args, **kwargs):
        self.user_type = 'Doctor'
        super(Doctor, self).save(*args, **kwargs)