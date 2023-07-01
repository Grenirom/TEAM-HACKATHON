from rest_framework import serializers

from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Favorite
        fields = '__all__'
