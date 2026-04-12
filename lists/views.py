from django.urls import path # Importe 'path' em vez de 'url'
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'), # Use path com string vazia para a raiz
]