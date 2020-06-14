from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    """
    API endpoint that allows Edereco.
    """
    queryset = Endereco.objects.all()#.order_by('-date_joined')
    serializer_class = EnderecoSerializer