from rest_framework import serializers
from ..models import Marca
from rest_flex_fields import FlexFieldsModelSerializer


class MarcaSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'