from django.db import models

class Sem_Lactose (models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

   