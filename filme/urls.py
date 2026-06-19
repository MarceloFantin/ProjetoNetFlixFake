#para cada pagina do site tem que construir 3 coisa
#url - link do pagina
#view - é o que vai acontecer(exmplo: vai pegar algo no banco de dado, fazer algum calculo...)
#template - é a parte visual HTML

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme, PesquisaFilme, PaginalPerfil
#biblioteca do django que ja tem view prontas
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    #liks das URLs
    path('', Homepage.as_view(), name="homepage"),
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', PesquisaFilme.as_view(), name="pesquisafilme"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarperfil/', PaginalPerfil.as_view(), name="editarperfil"),
]