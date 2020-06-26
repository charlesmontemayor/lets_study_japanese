from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from datetime import datetime

from .models import Guide


class GuideTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

        self.guide = Guide.objects.create(
            title='Test Title',
            body='This is a test body',
            author=self.user,
        )

        login = self.client.login(
            username='testuser',
            password='testpassword'
        )

    def test_string_representation(self):
        guide = Guide(title='Test Title')
        self.assertEqual(str(guide), guide.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.guide.get_absolute_url(), '/guides/test-title')

    def test_guide_slugify(self):
        self.assertEqual(self.guide.slug, 'test-title')

    def test_guide_content(self):
        self.assertEqual(f'{self.guide.title}', 'Test Title')
        self.assertEqual(f'{self.guide.body}', 'This is a test body')
        self.assertEqual(f'{self.guide.author}', 'testuser')

    def test_guide_list_view(self):
        response = self.client.get(reverse('guide_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test body')
        self.assertTemplateUsed(response, 'guides/guide_list.html')

    def test_guide_detail_view(self):
        response = self.client.get('/guides/test-title')
        no_response = self.client.get('/guides/no-slug')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'guides/guide_detail.html')

    def test_guide_create_view(self):
        response = self.client.post(reverse('guide_new'), {
            'title': 'New Title',
            'body': 'New body',
            'date': datetime.now(),
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Title')
        self.assertContains(response, 'New body')
