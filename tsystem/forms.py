from .models import *
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'type': 'text', 'name': 'username', 'id': 'username', 'pattern': '[а-яА-Яa-zA-Z0-9+-_.,@!#$%^&*]+', 'required': '','title': 'Имя может содержать только буквы'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'password', 'id': 'password', 'required': '', 'minlength': '8', 'maxlength': '128'}))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'name': 'first_name', 'required': '', 'id': 'firstname', 'pattern': '[а-яА-Яa-zA-Z]+', 'title': 'Имя может содержать только буквы'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'name': 'last_name', 'required': '', 'id': 'lastname', 'pattern': '[а-яА-Яa-zA-Z]+', 'title': 'Имя может содержать только буквы'})),
    email = forms.CharField(widget=forms.TextInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'example@example.com', 'required': '', 'id': 'ident', 'minlength': '6', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}', 'title': 'Следуйте указанному формату.'})),
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'name': 'username', 'required': '', 'id': 'username'})),
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password1', 'name': 'password1', 'id': 'password1', 'required': '', 'minlength': '8', 'maxlength': '128'})),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password2', 'name': 'password2', 'id': 'password2', 'required': '', 'minlength': '8', 'maxlength': '128'})),

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'username', 'password1', 'password2'}
        widgets = {
            'first_name': forms.TextInput(attrs={'type': 'text', 'name': 'first_name', 'required': '', 'id': 'firstname', 'pattern': '[а-яА-Яa-zA-Z]+', 'title': 'Имя может содержать только буквы'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'name': 'last_name', 'required': '', 'id': 'lastname', 'pattern': '[а-яА-Яa-zA-Z]+', 'title': 'Имя может содержать только буквы'}),
            'email': forms.TextInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'example@example.com', 'id': 'ident', 'minlength': '6','required': '', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}', 'title': 'Следуйте указанному формату.'}),
            'username': forms.TextInput(attrs={'type': 'text', 'name': 'username', 'required': '', 'id': 'username'}),
            'password1': forms.PasswordInput(attrs={'type': 'password1', 'name': 'password1', 'id': 'password1', 'required': '', 'minlength': '8', 'maxlength': '128'}),
            'password2': forms.PasswordInput(attrs={'type': 'password2', 'name': 'password2', 'id': 'password2', 'required': '', 'minlength': '8', 'maxlength': '128'}),
        }