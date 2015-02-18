# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

#    UserListView,
#    UserCreateView,
#    UserUpdateView,
#    UserDeleteView,
#    UserChangePasswordView,
#    GenerateRandomPasswordView
#)

urlpatterns = patterns(
    '',
    """
    url(r'^personal_mail/$',
        PersonalMailCreateView.as_view(),
        name='personal_mail'),
    url(r'^update/(?P<pk>\d+)/$',
        UserUpdateView.as_view(),
        name='update'),
    url(r'^delete/(?P<pk>\d+)/$',
        UserDeleteView.as_view(),
        name='delete'),
    url(r'^update_password/(?P<pk>\d+)/$',
        UserChangePasswordView.as_view(),
        name='update_password'),
    url(r'^random_password/(?P<pk>\d+)/$',
        GenerateRandomPasswordView.as_view(),
        name='generate_random_password'),
    """
)
