from ..models import Modelo
from ..Serializers.ser_modelo import ModeloSerializer
from rest_framework import viewsets



class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer