# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        verbose_name=_(u'profile owner')
    )

    brewery_shareholder = models.BooleanField(
        verbose_name=_(u'brewery shareholder')
    )

    def __unicode__(self):
        return self.user.get_full_name()
