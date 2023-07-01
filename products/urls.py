from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products import views
from products.views import ProductListCreate

urlpatterns = [
    path('list-create/', ProductListCreate.as_view()),
    path('detail-update-delete/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view()),
]
