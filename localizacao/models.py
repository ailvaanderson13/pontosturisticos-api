from django.db import models


class Localizacao(models.Model):
    linha1 = models.CharField(max_length=200, blank=True, null=True)
    linha2 = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.linha1

    class Meta:
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"