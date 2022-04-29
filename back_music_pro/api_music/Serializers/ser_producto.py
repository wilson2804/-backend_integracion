from ..models import Producto
from rest_flex_fields import FlexFieldsModelSerializer
from .ser_categoria import CategoriaSerializer
from .ser_modelo import ModeloSerializer


class ProductoSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'

        expandable_fields = {
        "categoria": (CategoriaSerializer, {"source": "categoria"}),
        "modelo": (ModeloSerializer, {"source": "modelo"})
    }

        