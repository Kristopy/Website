from django.test import SimpleTestCase

# Create your tests here.

class PagesTests(SimpleTestCase):
    def test_Home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_Phonons_page_status_code(self):
        response = self.client.get('/Phonons/')
        self.assertEqual(response.status_code, 200)
