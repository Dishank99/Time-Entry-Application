from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .forms import RegisterForm, LoginForm

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login-screen'),
    path('logout/', LogoutView.as_view(), name='logout-screen'),
    path('register/', RegisterView.as_view(), name='register-screen'),
]