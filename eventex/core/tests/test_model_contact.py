from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Marcelo Belli',
            slug='marcelo-belli',
            photo='https://photo.belli.me/marcelo-belli',

        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='marcelo@belli.me')
        self.assertTrue(Contact.objects.exists)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='41-8803-9137')
        self.assertTrue(Contact.objects.exists)

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact.objects.create(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='marcelo@belli.me')
        self.assertEqual('marcelo@belli.me', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Marcelo Belli',
            slug='marcelo-belli',
            photo='http://belli.me/marcelo-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='marcelo@belli.me')
        s.contact_set.create(kind=Contact.PHONE, value='41-8803-9137')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['marcelo@belli.me']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['41-8803-9137']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

