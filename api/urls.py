from django.urls import path
from .views import *

urlpatterns = [
    path("Autores", AutoresView.as_view()),
    path("Autores/<int:pk>", AutoresRetrieveUpdateDestroyAPIView.as_view()),
    path("Livros", LivrosView.as_view()),
    path("Livros/<int:pk>", LivrosRetrieveUpdateDestroyAPIView.as_view())
]

