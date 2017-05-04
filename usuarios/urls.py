from django.conf.urls import url
from django.contrib.auth.views.login import login, logout_then_login

from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    url(r'^registrar/$',  RegistrarUsuarioView.as_view(), name='registrar'),
    url(r'^login/$',  login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$',  logout_then_login,
        {'login_url': '/login/'}, name='login'),
]
