from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import Like
# from .serializers import LikeSerializer, LikeListSerializer


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated,)


class LikeListingView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


#
# class LikeCreateView(generics.CreateAPIView):
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class LikeDeleteView(generics.DestroyAPIView):
#     queryset = Like.objects.all()
#     permission_classes = (IsAuthenticated,)
#
#
# class LikeListingView(generics.ListAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeListSerializer
#
