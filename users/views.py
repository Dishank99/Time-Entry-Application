from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class UserLoginView(LoginView):
    template_name='users/login.html'
    authentication_form = LoginForm

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name='users/register.html'
    success_url = settings.LOGIN_URL
    success_message = 'Account created Successfully. Please Login to continue...'
