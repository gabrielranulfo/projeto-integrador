import unittest
from django.test.client import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Cada teste precisa de um cliente.
        self.client = Client()
        self.client.login(username='user_test', password='Mudar123')
    

    def test_api_get(self):
        response = self.client.get('/api/')
        self.failUnlessEqual(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get('/login/')
        self.failUnlessEqual(response.status_code, 200)

    def test_cadastro_setores_get(self):
        response = self.client.get('/cadastro_setores/')
        self.failUnlessEqual(response.status_code, 200)

    def test_cadastrar_setor_get(self):
        response = self.client.get('/cadastro_setores/')
        self.failUnlessEqual(response.status_code, 200)

    def test_create_setor_get(self):
        response = self.client.get('/cadastro_setores/')
        self.failUnlessEqual(response.status_code, 200)

    def test_cadastro_equipes_get(self):
        response = self.client.get('/cadastro_setores/')
        self.failUnlessEqual(response.status_code, 200)

    def test_cadastrar_equipes_get(self):
        response = self.client.get('/cadastro_setores/')
        self.failUnlessEqual(response.status_code, 200)


#https://django-portuguese.readthedocs.io/en/1.0/topics/testing.html#escrevendo-testes