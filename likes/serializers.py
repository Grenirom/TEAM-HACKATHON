from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    product = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        product = attrs['product']
        if user.likes.filter(product=product).exists():
            raise ValueError('You\'ve already liked this product!')
        return attrs

