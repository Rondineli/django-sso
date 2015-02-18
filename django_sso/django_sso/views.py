# -*- coding: utf-8 -*-
import logging

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied


class ViewPage(object):
    PAGE_NAME = ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ViewPage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ViewPage, self).get_context_data(*args, **kwargs)
        if 'page' not in context:
            context['page_name'] = self.PAGE_NAME
        return context
