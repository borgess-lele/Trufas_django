from django.db import models

class Combo (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    

class Sabor (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Sem_Lactose (models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
   
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


