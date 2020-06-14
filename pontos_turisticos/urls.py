"""pontos_turisticos URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.api.viewset import PontoTuristicoViewSet
from atracoes.api.viewset import AtracaoViewSet
from endereco.api.viewset import EnderecoViewSet
from comentarios.api.viewset import ComentarioViewSet
from avaliacoes.api.viewset import AvaliacaoViewSet
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'pontosTuristicos', PontoTuristicoViewSet,basename='PontosTuristicus')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
