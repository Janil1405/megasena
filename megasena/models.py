from django.db import models

class Sorteio(models.Model):
    data = models.DateField()
    numeros = models.CharField(max_length=20)

    def __str__(self):
        return f"Sorteio {self.data} - Números: {self.numeros}"
    
