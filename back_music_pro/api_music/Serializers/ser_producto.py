from ..models import Producto
from rest_flex_fields import FlexFieldsModelSerializer
from .ser_categoria import CategoriaSerializer
from .ser_modelo import ModeloSerializer
from rest_framework import serializers
from .ser_imagen import ImagenSerializer


class ProductoSerializer(FlexFieldsModelSerializer):
    imagen = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Producto
        fields = '__all__'

        expandable_fields = {
        "categoria": (CategoriaSerializer, {"source": "categoria"}),
        "modelo": (ModeloSerializer, {"source": "modelo"}),
        "imagen": (ImagenSerializer, {"source": "imagen", "many":True})
    }

        