from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Livro
from .serializers import AutorSerializers, LivroSerializers

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers

class AutoresRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers
    
class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

class LivrosRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers