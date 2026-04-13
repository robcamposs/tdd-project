from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # ESTE É O PASSO 7:
    def test_can_save_a_POST_request(self):
        # Envia um POST para a raiz '/' com os dados do formulário
        response = self.client.post('/', data={'item_text': 'A new list item'})
        
        # Verifica se o texto enviado aparece no HTML da resposta
        self.assertIn('A new list item', response.content.decode())
        
        # Opcional: Verifica se ainda estamos usando o template correto
        self.assertTemplateUsed(response, 'home.html')