from account.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('', AccountViewSet)

# router2 = DefaultRouter()
# router2.register('', ResetPasswordViewSet)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view()),
    # path('reset/', PasswordResetView.as_view()),
    path('detail-update/<int:pk>/', DetailUpdateUserView.as_view()),
    path('', include(router.urls)),
    path('reset/forgot/', ResetPasswordAPIVIew.as_view()),
    path('reset/confirm_reset/', ResetPasswordConfirmAPIView.as_view()),
]

