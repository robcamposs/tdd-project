from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        # ALTERE AQUI para verificar o erro proposital
        self.assertTemplateUsed(response, 'wrong.html')