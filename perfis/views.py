from django.shortcuts import render
from perfis.models import Perfil


# Create your views here.
def index(request):
    """Pagina Inicial"""
    return render(request, 'perfis\index.html')


def exibir(request, perfil_id):
    """View da pagina de Perfil"""
    if perfil_id == '1':
        perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '722',
                        'Caelum')

    return render(request, 'perfis\perfil.html', {"perfil": perfil})


