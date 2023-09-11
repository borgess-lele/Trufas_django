from django.db import models

class Combo (models.Model):
    nome = models.CharField(max_length=100)

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

