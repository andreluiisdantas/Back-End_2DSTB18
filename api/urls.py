from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("Autores/", views.listar_autores, name='listar-autores'),
    path("Autores/<int:pk>/", views.detalhes_autores, name='detalhes-autores'),
    path("Livros", LivrosView.as_view()),
    path("Livros/<int:pk>", LivrosRetrieveUpdateDestroyAPIView.as_view())
]

