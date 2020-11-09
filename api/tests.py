from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Person, Enterprise, Possession

class TestPersonAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(
            name='Fulano', cpf='999.999.999-99', birthday='2000-10-10'
        )
        self.new_person = {
            'name': 'Josefa', 'cpf': '000.000.000-00', 'birthday': '2020-01-01'
        }
        self.person_update = {
            'name': 'Maria', 'cpf': '111.111.111-11', 'birthday': '2019-01-01'
        }

    def test_person_list(self):
        response = self.client.get(reverse('api:person-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.person.name)

    def test_person_create(self):
        response = self.client.post(
            reverse('api:person-list'), self.new_person
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(
            Person.objects.get(id=2).name, self.new_person['name']
        )
    
    def test_person_post_bad_request(self):
        response = self.client.post(reverse('api:person-list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_person_update(self):
        response = self.client.put(
            reverse('api:person-detail', args=[self.person.pk]),
            self.person_update
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.person_update['name'])

    def test_person_delete(self):
        response = self.client.delete(
            reverse('api:person-detail', args=[self.person.pk])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestEnterpriseAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.enterprise = Enterprise.objects.create(
            name='ACME LTDA',
            owner_document='000.000.000-00', 
            fantasy_name='ACME',
            address='Rua das casas, 100'
        )
        self.new_enterprise = {
            'name': 'XPTO INC.',
            'owner_document': '000.000.000-00', 
            'fantasy_name': 'XPTO',
            'address': 'Rua das casas, 100'
        }
        self.enterprise_update = {
            'name': 'ACME LTDA',
            'owner_document': '99.999.999/9999-99', 
            'fantasy_name': 'ACME',
            'address': 'Rua das casas, 100'
        }
    
    
    def test_enterprise_list(self):
        response = self.client.get(reverse('api:enterprise-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_enterprise_create(self):
        response = self.client.post(
            reverse('api:enterprise-list'), self.new_enterprise
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Enterprise.objects.count(), 2)
        self.assertEqual(
            Enterprise.objects.get(id=2).name, self.new_enterprise['name']
        )
    
    def test_enterprise_post_bad_request(self):
        response = self.client.post(reverse('api:enterprise-list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_enterprise_update(self):
        response = self.client.put(
            reverse('api:enterprise-detail', args=[self.enterprise.pk]),
            self.enterprise_update
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.enterprise_update['name'])

    def test_enterprise_delete(self):
        response = self.client.delete(
            reverse('api:enterprise-detail', args=[self.enterprise.pk])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)