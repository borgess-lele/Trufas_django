from rest_framework.viewsets import ModelViewSet

from trufas.models import Combo, Sabor, Trufa
from trufas.serializers import ComboSerializer, SaborSerializer, TrufaSerializer, TrufaDetailSerializer,TrufaListSerializer

class ComboViewSet(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer

class SaborViewSet(ModelViewSet):
    queryset = Sabor.objects.all()
    serializer_class = SaborSerializer

class TrufaViewSet(ModelViewSet):
    queryset = Trufa.objects.all()

class TrufaViewSet(ModelViewSet):
    queryset = Trufa.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TrufaListSerializer
        elif self.action == "retrieve":
            return TrufaDetailSerializer
        return TrufaSerializer
    