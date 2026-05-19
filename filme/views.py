from django.shortcuts import render
from django.views import generic

from .models import Filme


# Create your views here.

#quando for criar as views pode se usar a function base view(FBV) que seria
#def homepage(request):
#    return render(request, 'homepage.html')
#usada para paginas mais simples quando quer somente mostrar um pagina e funcões simples da pagina
def homepage(request):
    return render(request, 'homepage.html')

#para paginas mais complexas usar class base view (CBV) tipo listar um elemento criado no models
#views orientadas a objeto
#class filmes(generic.ListView):
#    model = Filme

def homefilmes(request):
    lista_filmes = Filme.objects.all()
    context = {'lista_filmes': lista_filmes}
    return render(request, 'homefilmes.html', context)


