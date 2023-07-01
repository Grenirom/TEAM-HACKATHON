from account.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('', AccountViewSet)


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('detail-update/<int:pk>/', DetailUpdateUserView.as_view()),
    path('', include(router.urls)),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

