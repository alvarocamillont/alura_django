from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    ''' Classe de validação do formulário de registo de usuário '''
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro("Por Favor verifique os dados informados")
            valid = False
        else:
            user_exists = User.objects.filter(username=self.data['nome']).exists()

            if user_exists:
                self.adiciona_erro('Usuario ja existente')
                valid = False

        return valid

    def adiciona_erro(self, message):
            errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                             forms.utils.ErrorList())
            errors.append(message)
