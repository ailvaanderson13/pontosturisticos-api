from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from localizacao.api.serializers import LocalizacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = LocalizacaoSerializer(many=False)
    # criar chave no JSON com a informação que quiser do models que quiser
    chave_teste = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'comentarios', 'atracoes', 'endereco',
                  'chave_teste', 'desc_2')

    def get_chave_teste(self, obj):
        return f"{obj.descricao} - {obj.aprovado}"

