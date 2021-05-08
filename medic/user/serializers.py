from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Patient.objects.all(), message="Email already exists")])
    password = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Patient.objects.all(), message="user name already exists")])
    phone = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Patient.objects.all(), message="Phone already exists")])

    class Meta:
        model = Patient
        fields = ('name','username','email','password','address','state','country','phone','gender','height','weight','blood_group', 'genotype')
    
    def create(self, validated_data):
        patient = Patient.objects.create_user(**validated_data)
        return patient