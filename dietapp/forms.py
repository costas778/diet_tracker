from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import DietEntry

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class DietEntryForm(forms.ModelForm):
    class Meta:
        model = DietEntry
        fields = ['date', 'meal', 'calories']
