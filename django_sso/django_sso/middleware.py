# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from accounts.models import UserPersonalMail


class UserPersonalMailMiddleware(object):
    """
        Middleware for crate personal personal mail 
        This personal mail, will be used for recovery password and set new password
        
    """
    personal_mail_url = 'personal_mail'
    ignore_urls = ['/login', '/logout/', '/admin/']

    def process_request(self, request):
        if not request.user.is_authenticated():
            return None

        if request.session.get('is_personal_mail'):
            return None
        if request.path == reverse(self.personal_mail_url):
            return None

        if request.path in self.ignore_urls:
            print "ignore"
            return None

        if UserPersonalMail.objects.filter(user=request.user.pk).exists():
            request.session['is_personal_mail'] = True
            return None
        return redirect(self.personal_mail_url)
