from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializer
from . import custom_permission


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        # Автоматически устанавливаем текущего пользователя в качестве владельца заказа
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Возвращаем только заказы, принадлежащие текущему пользователю
        return self.queryset.filter(user=self.request.user)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, )


class OrderHistoryView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
