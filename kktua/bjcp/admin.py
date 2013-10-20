# -*- coding: utf-8 -*-
from django.contrib import admin
from bjcp.models import BJCPGuideline, Category, Style

admin.site.register(BJCPGuideline)
admin.site.register(Category)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'subcategory', 'low_og', 'high_og', 'low_fg', 'high_fg', 'low_abv', 'high_abv', 'low_ibu', 'high_ibu',
        'low_srm', 'high_srm')


admin.site.register(Style, StyleAdmin)