from django.shortcuts import render
#from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view

from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'signup': reverse('doctor:signup', request=request, format=format),
    })
    #reverse()
class DoctorSignup(generics.CreateAPIView):

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        #print(request.data)
        #print(serializer)
        if serializer.is_valid():
            doctor = serializer.save()
            if doctor:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response('no doctor')
        return Response(data=serializer.errors)