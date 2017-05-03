from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect


# Create your views here.
def index(request):
    """Pagina Inicial"""
    perfis = Perfil.objects.all()
    perfil_logado = get_perfil_logado(request)
    argumentos_view = {}
    argumentos_view['perfis'] = perfis
    argumentos_view['perfil_logado'] = perfil_logado
    return render(request, 'perfis\index.html', argumentos_view)


def exibir(request, perfil_id):
    """View da pagina de Perfil"""
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    eh_contato = perfil in perfil_logado.contatos.all()
    argumentos_view = {}
    argumentos_view['perfil'] = perfil
    argumentos_view['perfil_logado'] = perfil_logado
    argumentos_view['eh_contato'] = eh_contato

    return render(request, 'perfis\perfil.html', argumentos_view)


def convidar(request, perfil_id):
    """View da pagina de Perfil"""
    perfil_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidar)
    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id='1')


def aceitar(request, convite_id):
    """Aceite de convite"""
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
