from django.urls import path

from favorites.views import FavoriteCreateView, FavoriteListView, FavoriteDeleteView

urlpatterns = [
    path('create/', FavoriteCreateView.as_view()),
    path('list/', FavoriteListView.as_view()),
    path('delete/<int:pk>/', FavoriteDeleteView.as_view()),
]