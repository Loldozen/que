from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    SPECIALIZATION = (
        ('Cardiologist','Cardiologist'),
        ('Dental specialist','Dental specialist'),
        ('Dermatologist','Dermatologist'),
        ('Endocrinologist','Endocrinologist'),
        ('family medicine','family medicine'),
        ('Gastroenterology & Hepatologist','Gastroenterology & Hepatologist'),
        ('General Dentist','General Dentist'),
        ('General medicine','General medicine'),
        ('Geriatrician','Geriatrician'),
        ('Hematology','Hematology'),
        ('Infectious disease','Infectious disease'),
        ('Nephrologist','Nephrologist'),
        ('Neurologist','Neurologist'),
        ('Nuclear Physician ','Nuclear Physician '),
        ('Oncologist','Oncologist'),
        ('Ophthalmologist','Ophthalmologist'),
        ('Paediatrician','Paediatrician'),
        ('Pain physician','Pain physician'),
        ('Radiologist','Radiologist'),
        ('Radiotherapist','Radiotherapist'),
        ('Rheumatologist','Rheumatologist'),
        ('Urologist','Urologist'),
        ('Cardiothoracic & vascular surgery','Cardiothoracic & vascular surgery'),
        ('Dental Surgeon','Dental Surgeon'),
        ('ENT surgeon','ENT surgeon'),
        ('General surgeon','General surgeon'),
        ('Neurosurgeon','Neurosurgeon'),
        ('Orthopedics & Trauma surgeon','Orthopedics & Trauma surgeon'),
        ('Paediatric surgeon','Paediatric surgeon'),
        ('Plastic & Cosmetic Surgeon','Plastic & Cosmetic Surgeon'),
        ('Obstetrics & Gynecologist','Obstetrics & Gynecologist'),
        ('Psychiatrist','Psychiatrist'),
    )
    mdcn = serializers.IntegerField(
        required=True,
        validators=[UniqueValidator(queryset=Doctor.objects.all(), message="Email already exists")])
    phone = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Doctor.objects.all(), message="Phone already exists")])
    specialization = serializers.ChoiceField(choices=SPECIALIZATION, required=True)
    password = serializers.CharField(min_length=8)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Doctor.objects.all(), message="Email already exists")])

    def create(self, validated_data):
        #print(validated_data)
        #print("ahamd")
        #doctor = Doctor.objects.create_user(validated_data['email'], validated_data['password'], )
        doctor = Doctor.objects.create_user(validated_data['email'],validated_data['password'],validated_data)
        return doctor
    class Meta: 
        model = Doctor
        fields = ('mdcn', 'email', 'specialization','password', 'language', 'name','gender', 'phone')
    