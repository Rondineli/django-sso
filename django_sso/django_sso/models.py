# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DatedModel(models.Model):
    creation_time = models.DateTimeField(
        _(u'data de criação'),
        auto_now_add=True
    )
    modification_time = models.DateTimeField(
        _(u'data de atualização'),
        auto_now=True
    )

    class Meta:
        abstract = True
