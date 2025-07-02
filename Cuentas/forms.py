from django import forms
from .models import Profile
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'biografia', 'fecha_nacimiento']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'biografia', 'fecha_nacimiento', 'link']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
