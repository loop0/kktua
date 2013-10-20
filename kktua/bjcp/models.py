# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BJCPGuideline(models.Model):
    year = models.PositiveIntegerField(
        verbose_name=_(u'Guideline Year')
    )

    def __unicode__(self):
        return u'%s' % self.year

    class Meta:
        ordering = ('-year',)
        verbose_name = _(u'BJCP Guideline')
        verbose_name_plural = _(u'BJCP Guidelines')


class Category(models.Model):
    guideline = models.ForeignKey(
        BJCPGuideline,
        verbose_name=_(u'BJCP Guideline')
    )

    name = models.CharField(
        verbose_name=_(u'category name'),
        max_length=100
    )

    def __unicode__(self):
        return u'%s %s' % (self.id, self.name)

    class Meta:
        ordering = ('guideline', 'id')
        verbose_name = _(u'category')
        verbose_name_plural = _(u'categories')


class Style(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name=_(u'category')
    )

    subcategory = models.CharField(
        verbose_name=_(u'subcategory'),
        max_length=3
    )

    name = models.CharField(
        verbose_name=_(u'name'),
        max_length=100
    )

    aroma = models.TextField(
        verbose_name=_(u'aroma')
    )

    appearance = models.TextField(
        verbose_name=_(u'appearance')
    )

    flavor = models.TextField(
        verbose_name=_(u'flavor')
    )

    mouthfeel = models.TextField(
        verbose_name=_(u'mouthfeel')
    )

    impression = models.TextField(
        verbose_name=_(u'overral impression')
    )

    comments = models.TextField(
        verbose_name=_(u'comments')
    )

    history = models.TextField(
        verbose_name=_(u'history')
    )

    ingredients = models.TextField(
        verbose_name=_(u'ingredients')
    )

    examples = models.TextField(
        verbose_name=_(u'examples')
    )

    low_og = models.CharField(
        verbose_name=_(u'OG (low)'),
        max_length=5
    )

    high_og = models.CharField(
        verbose_name=_(u'OG (high)'),
        max_length=5
    )

    low_fg = models.CharField(
        verbose_name=_(u'FG (low)'),
        max_length=5
    )

    high_fg = models.CharField(
        verbose_name=_(u'FG (high)'),
        max_length=5
    )

    low_abv = models.CharField(
        verbose_name=_(u'ABV (low)'),
        max_length=5
    )

    high_abv = models.CharField(
        verbose_name=_(u'ABV (high)'),
        max_length=5
    )

    low_ibu = models.CharField(
        verbose_name=_(u'IBU (low)'),
        max_length=5
    )

    high_ibu = models.CharField(
        verbose_name=_(u'IBU (high)'),
        max_length=5
    )

    low_srm = models.CharField(
        verbose_name=_(u'SRM (low)'),
        max_length=50
    )

    high_srm = models.CharField(
        verbose_name=_(u'SRM (high)'),
        max_length=50
    )

    exceptions = models.TextField(
        verbose_name=_(u'stats exceptions'),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u'%s %s' % (self.subcategory, self.name)

    class Meta:
        ordering = ('category', 'subcategory')
        verbose_name = _(u'style')
        verbose_name_plural = _(u'styles')


