from rest_framework.serializers import ModelSerializer

from trufas.models import  Trufa

class TrufaSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = "__all__"
        depth = 1

class TrufaDetailSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = "__all__"
        depth = 1

class TrufaListSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = ["id", "titulo", "preco"]