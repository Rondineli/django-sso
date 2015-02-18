# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


from accounts.views import PersonalMailCreateView


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^accounts/',
        include(
            'accounts.urls',
            namespace='accounts'
        )),
    url(r'^personal_mail/$',
        PersonalMailCreateView.as_view(), name='personal_mail'),

    url(
        r'^$',
        include(
            'sso_request.urls',
            namespace='redirect_view'
        )),

    url(
        r'logout/$',
        'django.contrib.auth.views.logout', {
            'template_name': 'registration/logout.html'
        },
        name='logout'
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
)
