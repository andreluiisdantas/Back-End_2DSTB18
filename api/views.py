from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Livro
from .serializers import AutorSerializers, LivroSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

    
class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

class LivrosRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_autores(request,pk):

    autor = Autor.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = AutorSerializers(autor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        autor.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)