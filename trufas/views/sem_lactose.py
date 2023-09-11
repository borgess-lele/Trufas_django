from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from trufas.models import Sem_Lactose
from trufas.serializers import Sem_LactoseSerializer

class Sem_LactoseViewSet(ModelViewSet):
    queryset = Sem_Lactose.objects.all()
    serializer_class = Sem_LactoseSerializer