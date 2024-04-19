from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label= 'Email', required=True)
    