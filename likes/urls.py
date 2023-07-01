from django.urls import path

from likes.views import LikeCreateView, LikeDeleteView, LikeListingView

urlpatterns = [
    path('create/', LikeCreateView.as_view()),
    path('delete/<int:pk>/', LikeDeleteView.as_view()),
    path('list/', LikeListingView.as_view()),
]