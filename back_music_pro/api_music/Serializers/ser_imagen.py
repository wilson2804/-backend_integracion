from ..models import imagen
from rest_flex_fields import FlexFieldsModelSerializer

class ImagenSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = imagen
        fields = '__all__'