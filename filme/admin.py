from django.contrib import admin
from .models import Filme, Episodio, Usuario
#a biblioteca abaixo é para uma classe que vai gerenciar os usuarios
#tipo login, logout .....
from django.contrib.auth.admin import UserAdmin

#nesse caso o campo filmes_vistos criados da classe usuario não aparece automaticamente no
#no cadastro do usuario, pois esse campos do usuario vem do UserAdmin então temos que editar os canpos
#do UserAdmin colocando os campos extras
#os campos do UserAdmin são uma tupla então fazemos
campos = list(UserAdmin.fieldsets)
#primeiro item da tupla é o nome da sessão
#segundo item da tupla é um dicionario que tem como chave a expressão fields, e como valor uma
#tupla com o nome do campo(s) dentro
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.

admin.site.register(Filme)
admin.site.register(Episodio)
#para o usuario é diferente quando vai registrar no administrativo porque
#ja existe o usuario por padrão no django
#aqui passando o parementro UserAdmin diz para o django que quem vai gerenciar os usuario vai ser a
#classe usuario que criamos e não mais será criado pelo django os usuarios
#tem que alterar o setings.py
#passando uma varivel AUTH_USER_MODEL = 'filme.Usuario' - filme,usuario porque a classe esta dentro do APP filme

admin.site.register(Usuario, UserAdmin)



#depois de tudo configurado no settings.py tem que rodar o python .\manage.py makemigrations e
#python .\manage.py migrate aqui pode dar um erro porque ja tem um usuario criado no banco de dados
#como o campo que precisamos foi criado depois teremos que corrigir.
#se tivessemos feito o procedimendo criar uma classe para gerenciar o usuarios antes de ter um registro de usuario
#no banco de dados não teria dado nenhum erro.
#vamos tentar corrigir, mas se não der certo o bando de dados tem que ser apagado e os arquivos
#dentro da pasta migrations do os aquivos que tem numero o __init__.py da pasta não apaga
#para tentar corrigir vamos rodar
#passo 1 no settigns.py comentar a linha criada do AUTH_USER_MODEL =
#passo 2 e rodar no terminal python .\manage.py migrate auth zero ignorar se der erros
#passo 3 no settings.py desconmentar a linha criada do AUTH_USER_MODEL =
#passo 4 rodar no terminal python .\manage.py migrate auth
#como não deu certo vamos deletar o bando de dados ja que esta no começo da aplicação
#com o banco de dados deletado
#rodar no terminal para criar novamente o banco de dados
#python .\manage.py makemigrations e depois python .\manage.py migrate
#criar novamente o usuario
#python .\manage.py createsuperuser
#no usuario colocar email