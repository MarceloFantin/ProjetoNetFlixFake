from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, HomePageForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
#essa biblioteca serve para passar para as classbaseviews para bloquear a classbaseview se o usuario não estiver
#logado
from django.contrib.auth.mixins import LoginRequiredMixin


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

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomePageForm

    def get_success_url(self):
        email = self.request.POST.get('email')
        if Usuario.objects.filter(email=email).exists():
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

    def get(self, request, *args, **kwargs ):
        if request.user.is_authenticated:
            #aqui tem que usar o redirect não da para usar o render
            #no redirect tem que tem os paramentos nome do app:nome da pagina no caso filme:homefilme
            #lembrado que o nome do app não é o nome da pasta e sim o que esta configurado em urls.py app_name = 'filme'
            #e no urls.py também tem o nome da pagina
            return redirect('filme:homefilmes')

        else:
            return super().get(request, *args, **kwargs)  # redireciona o usuario para a URL final


# o LoginRequiredMixin sempre tem que estar no primero lugar dos paremetros
# para bloquear o acesso da pagina se não tiver logado
# e tem que alterar o settings.py para dizer para onde será redirecionado quando não conseguir entrar
# acrecentar as variaveis LOGIN_REDIRECT_URL e LOGIN_URL = '/login/'
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme


class Detalhesfilme(LoginRequiredMixin, DetailView):
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


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class PaginalPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email' ]

    def get_success_url(self):
        return reverse('filme:homefilmes')




class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    #essa função por padrão verifica se todos os campos foram preenchidos corretamente
    #mas nesse caso alem disso vai ser salvo o formulario
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    #essa função diz o que vai acontecer quando o formulário der certo
    #sempre que for criado um FormView tem que dizer para onde ir quando a função der certo
    #e é a get_success_url que faz isso
    def get_success_url(self):
        #essa função espera como resposta um url por isso não pode ser usado o redirect
        #tipo return redirect('filme:homefilmes') isso não vai dar erro
        #o correto é aqui é usar reverse
        #o reverse da como resposta o link correspondente
        return reverse('filme:homefilmes')









