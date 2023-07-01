from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        # fields = ('user_id', 'username')
        fields = '__all__'

    # def validate(self, attrs):
    #     user = self.context['request'].user
    #     print(attrs, '!!!!!!!!!!!!')
    #     product = attrs['product']
    #
    #         # if user.product_likes.filter(product=product).exists():
    #         #     raise serializers.ValidationError('you already liked this product')
    #     return attrs


class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
