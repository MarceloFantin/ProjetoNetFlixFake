from django.db import models
from django.utils import timezone

#na lista de categoria as tuplas detro da tupla tem que ser criada assim
#primeira informação é como é gravado no banco de dados
#segunda informação é como vai aparecer para o usuario
LISTA_CATEGORIA = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descrição = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criação = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo





# Create your models here.
