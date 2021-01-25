# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    User._meta.get_field('email').blank = False
    User._meta.get_field('username').blank = False
    User._meta.get_field('first_name').blank = False
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password', 'is_staff']
        widget = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control', 'maxlength': 255}),
            'username': forms.TextInput(attrs = {'class': 'form-control', 'maxlength': 255}),
            'email': forms.TextInput(attrs = {'class': 'form-control', 'maxlength': 255}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control', 'maxlength': 255}),
            'is_staff': forms.TextInput(attrs = {'class': 'form-control', 'maxlength': 255}),
        }

    def save(self, commit = True):
        user = super(UserModelForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user