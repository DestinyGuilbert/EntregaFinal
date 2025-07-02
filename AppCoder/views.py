from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AvatarForm, LoginForm
from .models import Avatar


from django.shortcuts import render


def test_template(request):
    return render(request, 'AppCoder/usuario/login.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def about(request):
    return render(request, 'AppCoder/about.html')

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'AppCoder/usuario/login.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Después de registrarse, va a login
    else:
        form = UserRegisterForm()
    return render(request, 'AppCoder/usuario/registro.html', {'form': form})



@login_required
def upload_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Cambia la url que necesites
    else:
        form = AvatarForm(instance=avatar)
    return render(request, 'AppCoder/usuario/upload_avatar.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'AppCoder/Cuentas/perfil.html', {'usuario': request.user})

@login_required
def editarPerfil(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "AppCoder/Cuentas/editar_perfil.html", {"form": form})

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'Cuentas/password_change.html'
    success_url = reverse_lazy('password_change_done')