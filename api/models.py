from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    biografia = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=255)
    data_publicacao = models.DateField(null=True, blank=True)
    autor = models.ManyToManyField(Autor)

    def __str__(self):
        return f"{self.titulo} {self.autor}"