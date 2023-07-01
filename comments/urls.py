from rest_framework.urls import path

from comments import views

urlpatterns = [
    path('create/', views.CommentCreateView.as_view()),
    path('list/', views.CommentListView.as_view()),
    path('delete/<int:pk>/', views.CommentDeleteView.as_view()),
]