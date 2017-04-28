from django.shortcuts import render
from perfis.models import Perfil


# Create your views here.
def index(request):
    """Pagina Inicial"""
    perfis = Perfil.objects.all()
    return render(request, 'perfis\index.html', {'perfis': perfis})


def exibir(request, perfil_id):
    """View da pagina de Perfil"""

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfis\perfil.html', {"perfil": perfil})
