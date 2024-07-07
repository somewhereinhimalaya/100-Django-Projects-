# why to create forms.py because we need other fields like first name last name and email

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# extending the form 
class SignUpForm(UserCreationForm):
    # customize UserCreationForm label in this place
    # there are password1 and password2 in UserCreationForm 
    # Changing label of password2 
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'} # changing the label name 