from django.db import models

from trufas.models import Sem_Lactose, Combo, Sabor

from django.db import models

class Trufa(models.Model):
    titulo = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    combo = models.ForeignKey(
        Combo, on_delete=models.PROTECT, related_name="trufa"
    )
    sem_lactose = models.ManyToManyField(Sem_Lactose, related_name="trufa")

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
