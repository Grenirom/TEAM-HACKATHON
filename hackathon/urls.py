from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from products.views import *


schema_view = get_schema_view(
   openapi.Info(
      title="MarketPlace API",
      default_version='v1',
      description="Test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('account/', include('account.urls')),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),
    path('likes/delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
    path('favorites/create/', FavoriteCreateView.as_view(), name='favorite-create'),
    path('favorites/delete/<int:pk>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
