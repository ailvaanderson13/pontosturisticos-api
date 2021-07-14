from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'descricao')
    lookup_field = 'nome'
