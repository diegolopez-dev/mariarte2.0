from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='Tienda'),
    path('tienda_carro', views.tienda_carro, name="TiendaCarro"),
]
