from django.urls import path
from mariarteApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
