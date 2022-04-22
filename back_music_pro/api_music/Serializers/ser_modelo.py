from rest_framework import serializers
from ..models import Modelo
from .ser_marca import MarcaSerializer
from rest_flex_fields import FlexFieldsModelSerializer



class ModeloSerializer(FlexFieldsModelSerializer):

    

    class Meta:
        model = Modelo
        fields = '__all__'

        expandable_fields = {
        "marca": (MarcaSerializer, {"source": "marca"})
    }
