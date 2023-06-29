from django.urls import path

from likes.views import LikeCreateView, LikeDeleteView

urlpatterns = [
    path('like-create/', LikeCreateView.as_view()),
    path('like-delete/', LikeDeleteView.as_view()),
]