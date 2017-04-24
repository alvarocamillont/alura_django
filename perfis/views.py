from django.shortcuts import render


# Create your views here.
def index(request):
    """Pagina Inicial"""
    return render(request, 'perfis\index.html')

