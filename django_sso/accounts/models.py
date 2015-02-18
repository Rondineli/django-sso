# -*- coding: utf-8 -*-
import re

from django.db import models
from django.core import validators
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django_sso.models import DatedModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = UserManager.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        if not password:
            password = self.make_random_password()
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_admin = True

        # TODO: add admin role
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, DatedModel):
    username = models.CharField(
        _('username'), max_length=30, unique=True,
        help_text=_(u'Obrigatório. 30 caracteres ou menos. Somente letras, '
                    u'dígitos e @/./+/-/_.'),
        validators=[
            validators.RegexValidator(
                re.compile(
                    '^[\w.@+-]+$'),
                _(u'Informe um nome de usuário válido.'),
                'invalid'
            )
        ]
    )
    name = models.CharField(_(u'nome'), max_length=80, db_index=True)
    phone = models.CharField(
        _(u'telefone'),
        max_length=18,
        null=True,
        help_text=_(u"Ex.: +55 11 91001 0101")
    )
    email = models.EmailField(_(u'email'), max_length=100, unique=True)
    is_active = models.BooleanField(_(u'está ativo'), default=True)
    is_admin = models.BooleanField(_(u'é admin'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.email

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class UserPersonalMail(DatedModel):
    personal_email = models.EmailField(
        _(u'email'),
        max_length=100,
        unique=True
    )
    user = models.ForeignKey('accounts.User')

    def __unicode__(self):
        return self.personal_email
