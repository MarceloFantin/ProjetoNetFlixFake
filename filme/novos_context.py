#aqui será criado todos os contextos que é usado em todas as paginas.
#esse gerenciador de contextos novos tem que ser configurados no setings.py em 'context_processors':[...]


from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    #esse filme destaque pode ser com outros tipos de filtro
    filme_destaque = lista_filmes[0]
    print(filme_destaque.titulo)
    print(filme_destaque.descricao)
    print(filme_destaque.thumb.url)
    print(filme_destaque.pk)
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}
