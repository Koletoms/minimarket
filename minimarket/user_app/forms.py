from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class AuthForm(forms.Form):
    """
    Форма аутентификации.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """
    Форма создания юзера и его профайла.
    """
    phone_number = forms.CharField(max_length=16, required=True)

    class Meta:
        model = User
        fields = "username", "first_name", "last_name", "email", "password1", "password2"
