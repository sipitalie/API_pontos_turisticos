from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    """
    API endpoint that allows Comentarios.
    """
    queryset = Avaliacao.objects.all()#.order_by('-date_joined')
    serializer_class =  AvaliacaoSerializer