from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
# Create your models here.
