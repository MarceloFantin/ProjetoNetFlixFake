#para cada pagina do site tem que construir 3 coisa
#url - link do pagina
#view - é o que vai acontecer(exmplo: vai pegar algo no banco de dado, fazer algum calculo...)
#template - é a parte visual HTML

from django.urls import path, include
from .views import homepage

urlpatterns = [
    #liks das URLs
    path('', homepage),
]