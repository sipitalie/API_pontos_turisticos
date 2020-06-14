from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco
# Create your models here.
class PontosTuristicus(models.Model):
    nome=models.CharField(max_length=50)
    descricao=models.TextField()
    aprovado=models.BooleanField(default=False)
    #atracoes=models.ManyToManyField(Atracao)
    #Comentarios=models.ManyToManyField(Comentario)
    avaliacao=models.ManyToManyField(Avaliacao)
    endereco=models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    atracoes = models.ForeignKey(Atracao, on_delete=models.CASCADE,null=True, blank=True)
    comentarios = models.ForeignKey(Comentario, on_delete=models.CASCADE,null=True, blank=True)
    foto=models.ImageField(upload_to='Pontos_turisticos',null=True, blank=True)

    def __str__(self):
        return self.nome
    