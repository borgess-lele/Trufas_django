from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from trufas.models import Trufa
from trufas.serializers import TrufaSerializer, TrufaListSerializer, TrufaDetailSerializer

class TrufaViewSet(ModelViewSet):
    queryset = Trufa.objects.all()


    def get_serializer_class(self):
        if self.action == "list":
            return TrufaListSerializer
        elif self.action == "retrieve":
            return TrufaDetailSerializer
        return TrufaSerializer
    