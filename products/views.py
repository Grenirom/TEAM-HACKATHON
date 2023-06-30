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




















from comments.models import Comment
from favorites.models import Favorite
from likes.models import Like
# # from .serializers import CommentSerializer, LikeSerializer, FavoriteSerializer
# from rest_framework.permissions import IsAuthenticated
#
#
# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class CommentUpdateView(generics.UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class CommentDeleteView(generics.DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class LikeCreateView(generics.CreateAPIView):
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class LikeDeleteView(generics.DestroyAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class FavoriteCreateView(generics.CreateAPIView):
#     serializer_class = FavoriteSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class FavoriteDeleteView(generics.DestroyAPIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     permission_classes = [IsAuthenticated]
# >>>>>>> d7cc0ea982cf7f00f8f313c2bd8a3f5254f0cded
