from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


class FavoriteCreateView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )


class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )


class FavoriteDeleteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )