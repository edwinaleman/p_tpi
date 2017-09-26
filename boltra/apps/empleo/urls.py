from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^inicio$', pagInicial, name='pag_inicio'), #url de prueba
]
