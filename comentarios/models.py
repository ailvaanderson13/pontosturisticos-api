from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.first_name

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"