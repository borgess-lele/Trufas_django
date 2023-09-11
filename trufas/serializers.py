from rest_framework.serializers import ModelSerializer

from trufas.models import Combo, Sabor, Trufa

class ComboSerializer(ModelSerializer):
    class Meta:
        model = Combo
        fields = "__all__"

class SaborSerializer(ModelSerializer):
    class Meta:
        model = Sabor
        fields = "__all__"

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