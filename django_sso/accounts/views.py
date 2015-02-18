# -*- coding: utf-8 -*-

from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from .models import UserPersonalMail
from .forms import PersonalMailForm


class PersonalMailCreateView(CreateView):
    PAGE_NAME = 'email pessoal'
    model = UserPersonalMail
    form_class = PersonalMailForm
    success_url = settings.DOMAIN_GOOGLE

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        messages.success(self.request, _(u'Cadastro efetuado com sucesso'))
        return super(PersonalMailCreateView, self).form_valid(form)

"""
class GenerateRandomPasswordView(View, SingleObjectMixin):
    model = User
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        password = User.objects.make_random_password()

        user.set_password(password)
        user.save()
        subject = _(u'Alteração de senha')
        message = _(
            u'Olá, {}. Sua senha no foi alterada para {}'.format(
                user.name,
                password
            )
        )
        user.email_user(subject, message)
        messages.success(self.request, _(u'Senha alterada com sucesso'))

        return redirect('accounts:list')


class UserChangePasswordView(View, SingleObjectMixin):
    model = User
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not password1 or not password2:
            messages.error(self.request, _(u'Preencha a senha'))
        elif len(password1) < 6:
            messages.error(
                self.request, _(u'A senha deve contem mais de 6 caracteres')
            )
        elif password1 != password2:
            messages.error(self.request, _(u'As senhas não conferem'))
        else:
            user.set_password(password1)
            user.save()
            messages.success(self.request, _(u'Senha alterada com sucesso'))

        return redirect('accounts:list')

    def form_valid(self, form):
        messages.success(self.request, _(u'Senha alterada com sucesso'))
        return super(UserChangePasswordView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _(u'Ocorreu algum erro ao alterar senha'))
        return redirect('accounts:list')
"""
