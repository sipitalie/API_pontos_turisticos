from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from core.models import PontosTuristicus
from .serializers import PontoTuristicuSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows PontosTuristicus.
    """
    #queryset = PontosTuristicus.objects.all()#.order_by('-date_joined')
    serializer_class = PontoTuristicuSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome','descricao','endereco__linha1']

    def get_queryset(self):
        return PontosTuristicus.objects.filter(aprovado=True)
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        saida={'teste':'sair'}
        return Response(saida)
