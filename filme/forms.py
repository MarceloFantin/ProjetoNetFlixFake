from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

#para criar um formulario de criação de usuarios
#esse é o padrão.
#Lembrado que aqui "Usuario" é a classe criada la em models que foi onde nos dizemos que
#essa classe seria a responsável pelo gerenciamento dos usuarios
class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']





