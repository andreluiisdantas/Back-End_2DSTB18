from django.shortcuts import render
from .models import Autor, Livro, Editora
from .serializers import AutorSerializers, LivroSerializers, EditoraSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# ==== View Autores ==== #
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
        
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
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
        
    elif request.method == 'PATCH': 
        serializer = AutorSerializers(autor, data = request.data, partial=True)
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
# ==== View Autores ==== #

# ==== View Editoras ==== #
@api_view(['GET', 'POST'])
def listar_editoras(request):
    if request.method == 'GET':
        queryset = Editora.objects.all()
        serializer = EditoraSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EditoraSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def detalhes_editoras(request,pk):

    editora = Editora.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = EditoraSerializers(editora)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = EditoraSerializers(editora, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH': 
        serializer = EditoraSerializers(editora, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        editora.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
# ==== View Editoras ==== #

# ==== View Livros ==== #
@api_view(['GET', 'POST'])
def listar_livros(request):
    if request.method == 'GET':
        queryset = Livro.objects.all()
        serializer = LivroSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LivroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def detalhes_livros(request,pk):

    livro = Livro.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = LivroSerializers(livro)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = LivroSerializers(livro, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = LivroSerializers(livro, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        livro.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
# ==== View Livros ==== #             