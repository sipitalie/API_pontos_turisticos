from comentarios.models import Comentario
from rest_framework.serializers import ModelSerializer 


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id','usuario','comentario','data']
