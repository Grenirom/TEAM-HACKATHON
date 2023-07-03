from rest_framework.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view()),
    path('history/<int:pk>/', views.OrderHistoryView.as_view()),
    path('list-all/', views.OrderListView.as_view()),
]