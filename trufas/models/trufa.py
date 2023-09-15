from django.db import models

from trufas.models import Sem_Lactose, Combo, Sabor

from django.db import models

from uploader.models import Image

class Trufa(models.Model):
    titulo = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, 
    decimal_places=2, default=0, null=True, blank=True)
    sabor = models.ForeignKey(
        Sabor, on_delete=models.PROTECT, related_name="trufa", null=True, blank=True
    )
    combo = models.ForeignKey(
        Combo, on_delete=models.PROTECT, related_name="trufa", null=True, blank=True
    )
    sem_lactose = models.ManyToManyField(Sem_Lactose, related_name="trufa", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
    
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
     )