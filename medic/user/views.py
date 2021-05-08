from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'signup': reverse('user:signup', request=request, format=format),
    })
    
class Signup(generics.CreateAPIView):

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        #print(request.data)
        #print(serializer)
        if serializer.is_valid():
            patient = serializer.save()
            if patient:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response('serializer did not save')
        return Response(data=serializer.errors)
