from django.test import TestCase

# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

# Django para visitar la página principal del sitio web (http://"pagina":8000, 
# donde your_server_ip es la dirección IP del servidor que utiliza). 
# Luego, el método de prueba comprueba si la respuesta tiene un código de estado 404, 
# lo que significa que la pagina no responde con errores
