from django.urls import path
from . import views

urlpatterns = [
    path('', views.verificar_combinacoes, name='verificar_combinacoes'),
]
