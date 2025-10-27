from django.test import TestCase, Client
from portfolio.models import About, Skill


class TemplatesSmokeTests(TestCase):
    def setUp(self):
        # Minimal objects to render templates
        About.objects.create(name='Tester', title='Dev', description='Desc', email='a@b.com')
        Skill.objects.create(name='Python', category='programming', level=90)

    def test_home_and_about_render(self):
        client = Client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)
        # Check that one category key appears in the rendered HTML
        self.assertIn('Langages', resp.content.decode('utf-8'))

        resp2 = client.get('/about/')
        self.assertEqual(resp2.status_code, 200)
        self.assertIn('Langages', resp2.content.decode('utf-8'))
