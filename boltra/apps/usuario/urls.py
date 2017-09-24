from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^estudiante$', Vuser.as_view(), name='reg_estudiante'),
    url(r'^empresa$', add_user, name='reg_empresa'),
    url(r'^inicio$', pagInicial, name='pag_inicial'), #url de prueba
]
