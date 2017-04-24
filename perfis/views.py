from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Pagina Inicial"""
    return render(request, 'perfis\index.html')

