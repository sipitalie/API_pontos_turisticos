from django.db import models
# Create your models here.

class Endereco(models.Model):
    linha1=models.CharField(max_length=150)
    linha2=models.CharField(max_length=150)
    cidade=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    latitude=models.FloatField(null=True, blank=True)
    longitude=models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.linha1
    


