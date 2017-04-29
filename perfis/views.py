from django.shortcuts import render
from perfis.models import Perfil
from django.shortcuts import redirect


# Create your views here.
def index(request):
    """Pagina Inicial"""
    return render(request, 'perfis\index.html', {'perfis': Perfil.objects.all()})


def exibir(request, perfil_id):
    """View da pagina de Perfil"""

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfis\perfil.html', {"perfil": perfil})


def convidar(request, perfil_id):
    """View da pagina de Perfil"""
    perfil_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidar)
    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id='1')
