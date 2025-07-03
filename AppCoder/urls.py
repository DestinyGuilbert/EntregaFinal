from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import inicio, login_request, register, editarPerfil, upload_avatar, logout_request, about
from AppCoder import views
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', inicio, name='inicio'),
    path('pages/', include('blog.urls')), 
    path('accounts/', include('Cuentas.urls')),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('editar-perfil/', editarPerfil, name='editar_perfil'),
    path('upload-avatar/', upload_avatar, name='upload_avatar'),
    path('logout/', logout_request, name='logout'),
    path('test-login/', views.test_template, name='test-login'),
    path('perfil/', views.perfil, name='perfil'),
    path('accounts/', include('Cuentas.urls')),
    path('mensajes/', include('Mensajes.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
