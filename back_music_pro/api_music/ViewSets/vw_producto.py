from ..models import Producto
from ..Serializers.ser_producto import ProductoSerializer
from rest_framework import viewsets
from api_music.authentication_mixins import Authentication



class ProductoViewSet(Authentication, viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        cat = self.request.query_params.get('cat', None)
        if cat is not None:
            queryset = queryset.filter(categoria=cat)
        return queryset