from django.db import models
from django.utils import timezone
#a biblioteca abaixo serve para importar o modelo de criação de usuario do django
from django.contrib.auth.models import AbstractUser
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

#quando usamos django todas as classes tem que ser registradas no admin.py
#para apercer no /admin do site
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descricao = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


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

#o usuario padrão do django ja tem varias campos
#aqui so vamos acrescentar os campos que vamor precisar
#como vamos gravar os filmes que o usuario va assistir vamos ter que adcionar
#outros campos no usuario
#todas as classes que criamos tem que registar no admin.py, mas essa classe será
#registrada um pouco diferente porque temos que dizer para o django que quem vai gerenciar
#os usuario é essa classe.
class Usuario (AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme", blank=True)

