from django.db import models
from django.utils import timezone
# Create your models here.

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
    descricao = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criação = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    #o parametro related_name cria um lista no tabela mãe no caso filme com todos os itens da tabela filha no caso
    #Episodio. Então da para acessar Filme.episodios
    filme = models.ForeignKey("Filme", related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo+ " - " + self.titulo
