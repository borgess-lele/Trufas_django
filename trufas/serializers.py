from rest_framework.serializers import ModelSerializer

from trufas.models import Combo

class ComboSerializer(ModelSerializer):
    class Meta:
        model = Combo
        fields = "__all__"