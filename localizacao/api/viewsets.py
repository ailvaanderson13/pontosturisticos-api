from rest_framework.viewsets import ModelViewSet
from localizacao.api.serializers import LocalizacaoSerializer
from localizacao.models import Localizacao


class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer