from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        '''Teste que verifica a autenticacao de um user com credenciais corretas'''

        user = authenticate(username='c3po', password='123456')

        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        '''Teste que verifica uma requisicao get nao autorizada'''

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        '''Teste que verifica a autenticacao de um user com username incorreto'''
        user = authenticate(username='c3po3', password='123456')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_de_user_com_password_incorreto(self):
        '''Teste que verifica a autenticacao de um user com passwword incorreto'''
        user = authenticate(username='c3po', password='12345')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_autenticado(self):
        '''Teste que verifica a requisicao get com o usuario autorizado'''
        self.client.force_authenticate(self.user)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
