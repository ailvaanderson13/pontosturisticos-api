from django.db import models
from atracoes.models import Atracao
from localizacao.models import Localizacao
from comentarios.models import Comentario


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    aprovado = models.BooleanField(default=True)
    atracoes = models.ManyToManyField(to=Atracao)
    comentarios = models.ManyToManyField(to=Comentario)
    endereco = models.ForeignKey(to=Localizacao, on_delete=models.DO_NOTHING, blank=True, null=True)

    @property
    def desc_2(self):
        return f"{self.descricao} - {self.aprovado}"

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ponto Turistico"
        verbose_name_plural = "Pontos Turisticos"
