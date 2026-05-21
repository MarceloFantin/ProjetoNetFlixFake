#para cada pagina do site tem que construir 3 coisa
#url - link do pagina
#view - é o que vai acontecer(exmplo: vai pegar algo no banco de dado, fazer algum calculo...)
#template - é a parte visual HTML

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme

app_name = 'filme'

urlpatterns = [
    #liks das URLs
    path('', Homepage.as_view(), name="homepage"),
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
]