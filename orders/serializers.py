from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = '__all__'

