from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),  # Toda la app principal bajo /
    path('accounts/', include('Cuentas.urls')),
    path('pages/', include('blog.urls')),
    path('accounts/', include('Cuentas.urls')),
    path('mensajes/', include('Mensajes.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


