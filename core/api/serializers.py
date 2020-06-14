from core.models import PontosTuristicus
from rest_framework.serializers import ModelSerializer 
from endereco.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicuSerializer(ModelSerializer):
    endereco=EnderecoSerializer()
    atracoes=AtracaoSerializer()
    comentarios=ComentarioSerializer()
    avaliacao=AvaliacaoSerializer(many=True)
    class Meta:
        model = PontosTuristicus
        fields = ['id', 'nome', 'descricao','avaliacao',
        'atracoes','comentarios','avaliacao','endereco','foto']
