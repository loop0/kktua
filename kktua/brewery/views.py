# -*- coding: utf-8 -*-
from django.views.generic import ListView
from brewery.models import Batch


class Statusboard(ListView):
    model = Batch
    template_name = 'statusboard.html'