from ..models import Categoria
from ..Serializers.ser_categoria import CategoriaSerializer
from rest_framework import viewsets



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer