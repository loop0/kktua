# -*- coding: utf-8 -*-
from django.contrib import admin
from brewery.models import Beer, Batch


admin.site.register(Beer)


class BatchAdmin(admin.ModelAdmin):
    list_display = ('beer', 'brewday', 'quantity', 'status')

admin.site.register(Batch, BatchAdmin)