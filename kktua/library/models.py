# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):

    name = models.CharField(
        verbose_name=_(u'first name'),
        max_length=100
    )

    surname = models.CharField(
        verbose_name=_(u'surname'),
        max_length=100
    )

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ('name', 'surname')
        verbose_name = _(u'author')
        verbose_name_plural = _(u'authors')


class Book(models.Model):

    author = models.ForeignKey(
        Author,
        verbose_name=_(u'book author'),
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        User,
        verbose_name=_(u'owner')
    )

    title = models.CharField(
        verbose_name=_(u'title'),
        max_length=100,
        blank=False
    )

    copies = models.PositiveIntegerField(
        verbose_name=_(u'copies'),
        default=1
    )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = _(u'book')
        verbose_name_plural = _(u'books')


class Borrowing(models.Model):

    borrowing_to = models.ForeignKey(
        User,
        verbose_name=_(u'person who borrowed')
    )

    book = models.ForeignKey(
        Book,
        verbose_name=_(u'borrowed book')
    )

    borrowing_date = models.DateField(
        verbose_name=_(u'borrowing date'),
        auto_now_add=True
    )

    return_date = models.DateField(
        verbose_name=_(u'return date'),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.book.title

    class Meta:
        ordering = ('-borrowing_date',)
        verbose_name = _(u'borrowing')
        verbose_name_plural = _(u'borrowings')

