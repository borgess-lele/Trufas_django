from rest_framework.viewsets import ModelViewSet

from trufas.models import Combo
from trufas.serializers import ComboSerializer

class ComboViewSet(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer