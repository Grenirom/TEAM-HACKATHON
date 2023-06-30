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
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('category/', include('category.urls')),
    path('comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('likes/create/', views.LikeCreateView.as_view(), name='like-create'),
    path('likes/delete/<int:pk>/', views.LikeDeleteView.as_view(), name='like-delete'),
    path('favorites/create/', views.FavoriteCreateView.as_view(), name='favorite-create'),
    path('favorites/delete/<int:pk>/', views.FavoriteDeleteView.as_view(), name='favorite-delete'),

]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

