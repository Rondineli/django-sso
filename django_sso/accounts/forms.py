# -*- coding: utf-8 -*-
"""
from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'username', 'email', 'phone', 'is_active', 'is_admin'
        )
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from django.template import loader

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from .models import User, UserPersonalMail


class PersonalMailForm(forms.ModelForm):
    class Meta:
        model = UserPersonalMail
        exclude = (
            'user',
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = (
            'is_active', 'is_admin', 'last_login'
        )
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254
    )

    def save(self, domain_override=None,
                subject_template_name='registration/password_reset_subject.txt',
                email_template_name='registration/password_reset_email.html',
                use_https=False, token_generator=default_token_generator,
                from_email=None, request=None):

        email = self.cleaned_data["email"]
        active_users = UserPersonalMail.objects.filter(
            personal_email__iexact=email,
            user__is_active=True
        )

        for user in active_users:
            print user.username
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            if domain_override:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [user.email])
