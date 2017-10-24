from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^inicio$', pagInicial, name='pag_inicio'), #url de prueba
    url(r'^registro_oferta$', regOferta, name='reg_oferta'), # Registrar oferta
    url(r'^mis_ofertas$', conOferta, name='con_oferta'), # Consultar mis ofertas
    url(r'^ofertas/(?P<id_ofertaempleo>\d+)/$', desOferta, name='des_oferta'), # Consultar oferta especifica
    url(r'^editar_oferta/(?P<id_ofertaempleo>\d+)/$', edtOferta, name='edt_oferta'), # Editar oferta
    url(r'^eliminar_oferta/(?P<id_ofertaempleo>\d+)/$', elmOferta, name='elm_oferta'), # Eliminar oferta
    url(r'^carreras/(?P<id_facultad>\d+)/$', lstCarrera, name='lst_carrera'), # Lista de carreras
    url(r'^ofertas_carrera/(?P<id_carrera>\d+)/$', conOfertaStd, name='con_oferta_std'), # Ofertas conusltadas por los estudiantes
]
