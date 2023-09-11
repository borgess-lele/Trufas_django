from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from trufas.models import Sabor
from trufas.serializers import SaborSerializer

class SaborViewSet(ModelViewSet):
    queryset = Sabor.objects.all()
    serializer_class = SaborSerializer
