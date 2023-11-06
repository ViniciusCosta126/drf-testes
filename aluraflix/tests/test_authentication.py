from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User()
