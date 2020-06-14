from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avaliacao(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comentario=models.TextField(null=True, blank=True)
    nota=models.DecimalField(max_digits=5, decimal_places=2)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    