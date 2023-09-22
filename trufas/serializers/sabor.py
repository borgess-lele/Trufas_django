from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from trufas.models import  Sabor
from uploader.serializers import ImageSerializer

class SaborSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Sabor
        fields = "__all__"