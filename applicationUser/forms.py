from django import forms 
from django.contrib.auth import get_user_model
from cuser.forms import UserCreationForm 
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2", ]

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", ]