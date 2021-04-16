from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username...'}),
        initial=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password...'})
    )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        strip=False,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name...'}),
    )
    last_name = forms.CharField(
        strip=False,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name...'}),
    )
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username...'}),
        initial=''
    )
    email = forms.CharField(
        widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        initial='',
    )
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password...'}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password...'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        help_texts = {
            'username':None,
            'password':None,
        }