from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("Autores/", views.listar_autores, name='listar-autores'),
    path("Autores/<int:pk>/", views.detalhes_autores, name='detalhes-autores'),
    
    path("Editoras/", views.listar_editoras, name='listar-editoras'),
    path("Editoras/<int:pk>/", views.detalhes_editoras, name='detalhes-editoras'),

    path("Livros/", views.listar_livros, name='listar-livros'),
    path("Livros/<int:pk>/", views.detalhes_livros, name='detalhes-livros'),
]

