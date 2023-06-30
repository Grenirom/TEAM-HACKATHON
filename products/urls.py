from django.urls import path

from products.views import *
urlpatterns = [
    path('list-create/', ProductListCreateView.as_view()),
    path('detail-update-delete/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
]