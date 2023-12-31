from rest_framework.serializers import ModelSerializer, SlugRelatedField

from trufas.models import  Trufa

from uploader.models import Image
from uploader.serializers import ImageSerializer

class TrufaSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = "__all__"
        depth = 1

        capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

class TrufaDetailSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)

class TrufaListSerializer(ModelSerializer):
    class Meta:
        model = Trufa
        fields = ["id", "titulo", "preco"]