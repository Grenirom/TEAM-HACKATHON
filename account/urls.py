from account.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('', AccountViewSet)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('', include(router.urls)),
]

