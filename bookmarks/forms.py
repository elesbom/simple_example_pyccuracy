#coding:utf-8

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.util import ErrorList

import re

class RegistrationForm(forms.Form):
    username = forms.CharField(label= "Nome do usuário", max_length=30)
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label="Repetir senha",
        widget=forms.PasswordInput(),
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('As senhas não conferem.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('O nome do usuário só pode conter \
                caracteres alfanuméricos e underline.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Este usuário está em uso, por favor \
            tente outro.')
