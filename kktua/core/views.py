# -*- coding: utf-8 -*-
from django.shortcuts import render


def statusboard(request):

    return render(request, 'statusboard.html')
