from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListingSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ('title', 'image', 'price')














# from .models import Comment, Like, Favorite


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'user', 'product', 'content', 'created_at')
#
#
# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ('id', 'user', 'product')
#
#
# class FavoriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favorite
#         fields = ('id', 'user', 'product')
