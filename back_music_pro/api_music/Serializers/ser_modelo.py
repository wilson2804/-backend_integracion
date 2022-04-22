from rest_framework import serializers
from ..models import Modelo
from .ser_marca import MarcaSerializer



class ModeloSerializer(serializers.ModelSerializer):

    marca = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Modelo
        fields = '__all__'

        expandable_fields = {
        "marca": (MarcaSerializer, {"source": "marca"})
    }
