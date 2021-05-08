from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view

from .models import Doctor
from .serializers import DoctorSerializer, LoginSerializer

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


class Login(APIView):

    def post(self, request, format=None):

        context = {}
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():

            try:
                email = serializer.data['email']
                password = serializer.data['password']
            except KeyError:
                return Response({'error': 'All credentials must be provided'}, status=status.HTTP_400_BAD_REQUEST)
            doctor = authenticate(email=email, password=password)
            if doctor:
                token = reverse('doctor:obtain_token', kwargs={'email':email, 'password':password})
                context['response'] = 'Login successful'
                context['email'] = email
                context['token'] = token.access
                context['refresh'] = token.refresh
            else:
                context['response'] = 'Error'
            return Response(context)
        else:
            return Response('serializer is not valid')