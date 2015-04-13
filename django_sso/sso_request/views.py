# -*- coding: utf-8 -*-
import os

from saml_response import SAML2Response
from django.conf import settings
from django.views.generic import View
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy

from django_sso.views import ViewPage


class AssertView(ViewPage, View):
    """
        Class for post on data in sso request
        and redirect session for google apps
    """
    success_url = reverse_lazy('redirect_view')
    try:
        private_key_file_name = settings.SAML2IDP_PRIVATE_KEY_FILE
    except AttributeError:
        private_key_file_name = os.path.join(
            settings.BASE_DIR,
            'keys/rsaprivkey.pem'
        )

    try:
        certificate_file_name = settings.SAML2IDP_CERTIFICATE_FILE
    except AttributeError:
        certificate_file_name = os.path.join(
            settings.BASE_DIR,
            'keys/rsacert.pem'
        )

    def get(self, request, *args, **kwargs):
        self.saml_resp = SAML2Response(
            private_key_file_name=self.private_key_file_name,
            certificate_file_name=self.certificate_file_name
        )
        saml_response, resp_url = self.saml_resp.get_login_response(
            request,
            request.user.username
        )
        token = request.GET.get('RelayState', None)
        return render_to_response(
            'saml2idp/sso_post_response.html', {
                'response_url': resp_url,
                'saml_response': saml_response,
                'token': token,
            }
        )
