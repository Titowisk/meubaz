# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_status_code(self):
        # should be 200
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

        
class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contact_section.html')

    def test_form_blank(self):
        data = {'name': '', 'email': '', 'message': ''}
        response = self.client.post(self.url, data)
        # .assertFormError(response, form, field, errors, msg_prefix='')
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_form_invalid_input(self):
        data = {'name': 'Vitor', 'email': 'contato@.com', 'message': 'Teste'}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Informe um endereço de email válido.')

    def test_form_email(self):
        data = {'name': 'Vitor', 'email': 'contato@meubaz.com', 'message': 'Teste'}
        response = self.client.post(self.url, data)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do MeuBaz')
        self.assertEquals(mail.outbox[0].from_email, 'admin@meubaz.com.br')
        # .assertRedirects(response, expected_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertRedirects(response, '/sucesso/')








"""
To know more abou the .assertSomething stuff:
https://docs.python.org/3/library/unittest.html#unittest.TestCase

And to know how the Python assert testing works in Django go to:
https://docs.djangoproject.com/en/1.11/topics/testing/tools/#assertions
"""