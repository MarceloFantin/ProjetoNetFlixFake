from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView

from .models import Filme


# Create your views here.

#quando for criar as views pode se usar a function base view(FBV) que seria

#def homepage(request):
#    return render(request, 'homepage.html')
#
# def homefilmes(request):
#     lista_filmes = Filme.objects.all()
#     context = {'lista_filmes': lista_filmes}
#     return render(request, 'homefilmes.html', context)
#usada para paginas mais simples quando quer somente mostrar um pagina e funcões simples da pagina

#para paginas mais complexas usar class base view (CBV) tipo listar um elemento criado no models
#views orientadas a objeto
#nesse projeto sera usado CBV

class Homepage(TemplateView):
    template_name = 'homepage.html'

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme

class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme









