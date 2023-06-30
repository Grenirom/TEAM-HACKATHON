from rest_framework import generics, permissions

from products.models import Product
from products.serializers import ProductSerializer, ProductListingSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductSerializer
        elif self.request.method == 'GET':
            return ProductListingSerializer

    def get_permission_classes(self):
        if self.request.method == 'GET':
            return permissions.AllowAny
        elif self.request.method == 'POST':
            return permissions.IsAdminUser


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

