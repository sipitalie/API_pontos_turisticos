from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework import filters

class AtracaoViewSet(ModelViewSet):
    """
    API endpoint that allows Atracoes.
    """
    queryset = Atracao.objects.all()#.order_by('-date_joined')
    serializer_class = AtracaoSerializer
    #filter_backends = [filters.SearchFilter]
    filterset_fields = ['nome', 'descricao']
    #search_fields = ['nome','descricao','endereco__linha1']




    


