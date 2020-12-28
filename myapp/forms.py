from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model


User = get_user_model()
class SignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
