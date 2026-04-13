from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        # 1. Envia o POST
        response = self.client.post('/', data={'item_text': 'A new list item'})
        
        # 2. Verifica se o texto está no HTML
        self.assertIn('A new list item', response.content.decode())
        
        # 3. O AJUSTE: Verifica se usou o template home.html
        self.assertTemplateUsed(response, 'home.html')