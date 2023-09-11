from rest_framework.serializers import ModelSerializer

from trufas.models import Sem_Lactose

class Sem_LactoseSerializer(ModelSerializer):
    class Meta:
        model = Sem_Lactose
        fields = "__all__"