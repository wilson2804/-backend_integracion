
from ..models import Categoria
from rest_flex_fields import FlexFieldsModelSerializer


class CategoriaSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        
        expandable_fields = {'parent': 'api_music.CategoriaSerializer'}
        


        

        

