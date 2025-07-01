from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar
 
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="Ingrese su email:")
    # password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label="Nombre de usuario")

    last_name = forms.CharField()
    first_name = forms.CharField()
    is_active = forms.BooleanField(required=False, label="¿Está activo?")

    class Meta:
        model = User
        # fields = ('email', 'password')
        fields = ('username', 'email', 'last_name', 'first_name', 'is_active')


class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']
