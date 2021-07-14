from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario = models.TextField()
    idade_min = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"
