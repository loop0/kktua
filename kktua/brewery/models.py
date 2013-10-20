# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from bjcp.models import Style


class Beer(models.Model):
    style = models.ForeignKey(
        Style,
        verbose_name=_(u'beer style'),
        blank=True,
        null=True
    )

    name = models.CharField(
        verbose_name=_(u'beer name'),
        max_length=100
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Batch(models.Model):
    FERMENTING = 1
    MATURING = 2
    READY = 3

    STATUS = (
        (FERMENTING, _(u'fermenting')),
        (MATURING, _(u'maturing')),
        (READY, _(u'ready'))
    )

    STATUS_LABEL = {
        FERMENTING: 'label-danger',
        MATURING: 'label-warning',
        READY: 'label-success'
    }

    beer = models.ForeignKey(
        Beer,
        verbose_name=_(u'beer brewed')
    )

    quantity = models.PositiveIntegerField(
        verbose_name=_(u'quantity brewed'),
        help_text=_(u'in liters')
    )

    brewday = models.DateField(
        verbose_name=_(u'brewday')
    )

    status = models.PositiveIntegerField(
        verbose_name=_(u'beer status'),
        choices=STATUS,
        default=FERMENTING
    )

    def get_status_label(self):
        return self.STATUS_LABEL[self.status]

    def __unicode__(self):
        return self.beer.name

    class Meta:
        ordering = ('-brewday', 'beer')
        verbose_name = _(u'batch')
        verbose_name_plural = _(u'batches')

