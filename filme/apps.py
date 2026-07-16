from django.apps import AppConfig


class FilmeConfig(AppConfig):
    name = 'filme'
    #foi criado umaa View para criar super usuario
    #mas poderia ser feito assim
    #essa funçao roda depois que o FilmeConfig e rodado
    def ready(self):
        from .models import Usuario
        import os
        #criar no projeto duas variaveis de ambiente com o e-mail do usuario e a senha
        #pegar essa variaveis
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")
        #verificar se exite um usuario com esse e-mail
        usuario = Usuario.objects.filter(email=email)
        if not usuario:
            Usuario.objects.create_superuser(username="admin", email=email, password=senha,
                                             is_active=True, is_staff=True, is_superuser=True)
            print('Superuser criado')
