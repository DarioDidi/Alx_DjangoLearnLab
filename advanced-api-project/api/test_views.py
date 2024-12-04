import json

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Book, Author
from .views import *
from .serializers import AuthorSerializer


class createBook(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            "user1", "address@email.com", "user1@pwd")
        self.user = user
        author = Author.objects.create(name='a1')
        author.save()
        self.author = author
        # token for auth
        token, created = Token.objects.get_or_create(user=self.user)
        self.token = token
        book = Book.objects.get_or_create(
            {'title': 'b1', 'publication_year': 2000, 'author': self.author})
        print("book", book)
        self.book = book

    # test user logged in
    def test_loggedin(self):
        self.assertTrue(self.client.login(
            username='user1', password='user1@pwd'))

    #test get details view
    def test_get(self):
        url = reverse('detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
    
    # test book creation
    def test_creation(self):
        url = reverse('create')

        data = {'title': 'book2', 'publication_year': 2000, 'author': 1}
        response = self.client.post(url, data, format='json',  headers={
                                    'Authorization': 'Token {}'.format(self.token)})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content.decode(
        ), '{"id":2,"title":"book2","publication_year":2000,"author":1}')

    # test object updates
    def test_update(self):
        url = reverse('update', kwargs={'pk': 1})
        data = {'title': 'b1_v2', 'publication_year': 2010, 'author': 1}
        response = self.client.put(url, data, format='json',  headers={
            'Authorization': 'Token {}'.format(self.token)})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], response.data['title'])
        self.assertEqual(data['publication_year'], response.data['publication_year'])

    # test object delete
    def test_delete(self):
        url = reverse('delete', kwargs={'pk': 1})
        response = self.client.delete(url, format='json',  headers={
            'Authorization': 'Token {}'.format(self.token)})
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)
