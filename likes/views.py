from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from . import serializers
from .models import Like
# from .permissions import IsAuthor


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (AllowAny, )