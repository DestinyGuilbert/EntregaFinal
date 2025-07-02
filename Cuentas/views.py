from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Profile
from .forms import ProfileEditForm, UserEditForm

@login_required 
def perfil_view(request):
    perfil = request.user.perfil
    return render(request, "AppCoder/Cuentas/perfil.html", {"perfil": perfil})

@login_required
def editar_perfil(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(usuario=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'AppCoder/Cuentas/editar_perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def password_change_done(request):
    return render(request, 'AppCoder/Cuentas/password_change_done.html')

# Create your views here.

@login_required
def perfil(request):
    user = request.user
    try:
        profile = user.profile  # gracias al related_name='profile'
    except Profile.DoesNotExist:
        profile = Profile.objects.create(usuario=user)

    return render(request, 'AppCoder/Cuentas/perfil.html', {
        'user': user,
        'profile': profile,
    })


@login_required
def about(request):
    profile, created = Profile.objects.get_or_create(usuario=request.user)
    user = request.user
    return render(request, 'AppCoder/about.html', {
        'profile': profile,
        'user': user,
    })