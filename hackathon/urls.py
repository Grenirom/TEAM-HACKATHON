"""
URL configuration for hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    LikeCreateView,
    LikeDeleteView,
    FavoriteCreateView,
    FavoriteDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('account/', include('account.urls')),

=======
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),
    path('likes/delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
    path('favorites/create/', FavoriteCreateView.as_view(), name='favorite-create'),
    path('favorites/delete/<int:pk>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
>>>>>>> c662b3bd430f17f0c0a3de4ec601a76ad37231c5
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
