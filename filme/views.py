from django.contrib.auth import user_logged_in
from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from .models import Filme, Usuario


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

    #vamos fazer um contagem de visuzalizações
    #nesse caso será contabilizado quando entrar no detalhes do filme
    def get(self, request, *args, **kwargs):
        #descobrir qual filme esta sendo acessado
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        usuario.save()
        # print('passou aqui')
        return super().get(request, *args, **kwargs) #redireciona o usuario para a URL final


    #aqui no Detalhesfilme teremos que ter outra view
    #então tem que ter a função abaixo, pois nas DetailView por padrão sempre tem somente uma View
    def get_context_data(self, **kwargs):
        #essa linha garante que a contexto original a view original não seja apagada
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtrar os filmes cujo a categoria é igual a categoria do filme do detalhe
        filmes_relacionados = self.model.objects.filter(categoria = self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        #print("passou aqui 2")
        return context


class PesquisaFilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None










