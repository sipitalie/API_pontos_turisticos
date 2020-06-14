from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    """
    API endpoint that allows Comentarios.
    """
    queryset = Comentario.objects.all()#.order_by('-date_joined')
    serializer_class = ComentarioSerializer