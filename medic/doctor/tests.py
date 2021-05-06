from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Doctor
from rest_framework import status

class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        self.test_doctor = Doctor.objects.create_user(email='test@example.com',password='testpassword', mdcn=1234, language='english')

        # URL for creating an account.
        self.create_url = reverse('doctor:signup')

    def test_create_doctor(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'mdcn': 4567,
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'language':'english'
        }

        response = self.client.post(self.create_url , data, format='json')


        # We want to make sure we have two users in the database..
        self.assertEqual(Doctor.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['mdcn'], data['mdcn'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)