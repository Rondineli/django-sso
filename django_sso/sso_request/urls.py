# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib import admin

from views import AssertView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', AssertView.as_view(), name='redirect'),
)
