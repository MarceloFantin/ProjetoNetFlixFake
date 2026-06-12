#aqui será criado todos os contextos que é usado em todas as paginas.
#esse gerenciador de contextos novos tem que ser configurados no setings.py em 'context_processors':[...]


from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    #esse filme destaque pode ser com outros tipos de filtro
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}
