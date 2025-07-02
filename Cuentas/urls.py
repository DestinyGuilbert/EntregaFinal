from django.urls import path
from AppCoder.views import login_request, register, logout_request, perfil, CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from . import views
from .views import password_change_done, editar_perfil
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('', login_request, name='accounts_home'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_request, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar-perfil'),
    path('about/', views.about, name='about'),
    path('password_change/', PasswordChangeView.as_view(template_name='AppCoder/Cuentas/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='AppCoder/Cuentas/password_change_done.html'), name='password_change_done'),

]
