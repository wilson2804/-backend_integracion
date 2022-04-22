from ..models import Marca
from ..Serializers.ser_marca import MarcaSerializer
from rest_framework import viewsets



class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer