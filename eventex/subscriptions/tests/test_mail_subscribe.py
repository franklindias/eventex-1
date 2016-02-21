from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Manaia Junior', cpf='12345678901', email='manaiajr.ifrn@gmail.com', phone='84-98892-9399')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'manaiajr.ifrn@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Manaia Junior',
            '12345678901',
            'manaiajr.ifrn@gmail.com',
            '84-98892-9399',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)