from rest_framework.serializers import ModelSerializer

from trufas.models import Combo

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer


class ComboSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Combo
        fields = "__all__"

class ComboDetailSerializer(ModelSerializer):
        capa = ImageSerializer(required=False)
