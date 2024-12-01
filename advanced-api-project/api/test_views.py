from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Book, Author
from .views import *

class createBook(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            "user1", "address@email.com", "user1@pwd")
        self.user = user
        author = Author.objects.create(name='a1')
        author.save()

    # self.client

    def test_loggedin(self):
        self.assertTrue(self.client.login(
            username='user1', password='user1@pwd'))

    def test_creation(self):
        url = reverse('create')
        # token = Token.objects.get_or_create(user_id='1')
        token, created = Token.objects.get_or_create(user=self.user)
        print(token)
        data = {'title': 'b1', 'publication_year': 2000, 'author': 1}
        response = self.client.post(url, data, format='json',  headers={
                                    'Authorization': 'Token {}'.format(token)})
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update(self):
    #     url = reverse('update', args={'pk': 1})
    #     # url =" books/update/1/"
    #     # url = reverse('update')
    #     token, created = Token.objects.get_or_create(user=self.user)
    #     data = {'title': 'b1_v2', 'publication_year': 2010, 'author': 1}
    #     response = self.client.put(url, data, format='json',  headers={
    #                                 'Authorization': 'Token {}'.format(token)})
    #     print(response)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_w_factory(self):
        factory = APIRequestFactory()    
        
        url = reverse('update', kwargs={'pk': 1})
        # url =" books/update/1/"
        
        token, created = Token.objects.get_or_create(user=self.user)
        data = {'title': 'b1_v2', 'publication_year': 2010, 'author': 1}
        request = factory.put(url, data, format='json',  headers={
                                    'Authorization': 'Token {}'.format(token)})
        view =  UpdateView.as_view()
        response = view(request, pk=1)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)