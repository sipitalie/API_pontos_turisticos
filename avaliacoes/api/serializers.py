from avaliacoes.models import Avaliacao
from rest_framework.serializers import ModelSerializer 


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id','user','comentario','nota','data']
 