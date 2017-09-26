# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def pagInicial(request):
	return render(request, 'inicio.html')