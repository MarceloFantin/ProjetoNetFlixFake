#para cada pagina do site tem que construir 3 coisa
#url - link do pagina
#view - é o que vai acontecer(exmplo: vai pegar algo no banco de dado, fazer algum calculo...)
#template - é a parte visual HTML
from django.contrib.messages.api import success
from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, PesquisaFilme, PaginalPerfil, CriarConta, criar_admin_temp
#biblioteca do django que ja tem view prontas
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    #liks das URLs
    # auth_views são views padrões do django que aqui foi mudado para o nome auth_views na importação do
    #bibliteca na acima from django.contrib.auth import views as auth_views
    path('', Homepage.as_view(), name="homepage"),
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', PesquisaFilme.as_view(), name="pesquisafilme"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarperfil/<int:pk>', PaginalPerfil.as_view(), name="editarperfil"),
    path('criarconta/', CriarConta.as_view(), name="criarconta"),
    #como o mudar senha o HTML vai ser igual o ediar perfil será usado o mesmo HTML
    #no PasswordChangeView também precisa de uma success_url que á passado nos parametros
    #no paremetro tem que user o reverse_lazy diferente na função que usa so o reverse
    path('mudarsenha/' , auth_views.PasswordChangeView.as_view(template_name="editarperfil.html",
                                                                    success_url=reverse_lazy('filme:homefilmes')), name="mudarsenha"),

    #url para criar o usuario quado o projeto estiver no ar porque o reder usado é free
    #comentar depois de criar o usuario para não ficar em produção
    path('criar-admin-temp/', criar_admin_temp, name='criar_admin_temp'),
]