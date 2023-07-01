from rest_framework import serializers

from likes.models import Like
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# def to_representation(self, instance):
#     rep = super().to_representation(instance)
#     # print(instance.likes)
#     res['hello']
#     print(rep)
#     print('!!!!!!!!!!!')
#     return rep


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'


# class ProductListingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         # fields = ('id', 'title', 'creator', 'image', 'desc', 'price')
#         fields = '__all__'
#
#
#     def to_representation(self, instance):
#         # print(instance, '!!!!!!!!!!!!!!!!!!!!!1')
#         repr = super(ProductListingSerializer, self).to_representation(instance)
#         # repr['count_of_likes'] = instance.product_likes.count()
#         print('!!!!!!!!!!!!!!')
#         print(repr)
#         return repr
