from uuid import uuid4

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from account.send_mail import send_activation_code, send_password_change_mail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *

User = get_user_model()


class AccountViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_activation_code(user.email, user.activation_code)
            except Exception:
                return Response({'msg': 'Registered, but issues with email', 'data': serializer.data}, status=201)
        return Response(serializer.data, status=201)

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except:
            return Response({"msg": 'Invalid link, or link has expired!'}, status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Successfully registered!'}, status=200)

    @action(['POST'], detail=False)
    def forgot(self, request, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_password_change_mail(user.email)
            except Exception as e:
                print(e, '************************')
                return Response({'msg': 'Issues with email!'})
            return Response({'msg': 'The reset mail was sent to your email address!'}, status=200)

    @action(['POST'], detail=False, url_path='confirm_reset/(?P<uuid>[0-9A-Fa-f-]+)')
    def confirm_reset(self, request, uuid):
        code = str(uuid4())
        serializer = ConfirmResetSerializer(data=request.data, context={'reset_code': uuid})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            user = User.objects.create(reset_code=code)
        except:
            return Response({"msg": 'Invalid link, or link has expired!'}, status=400)
        user.set_password(serializer.password)
        user.reset_code = ''
        user.save()
        return Response({'msg': 'Successfully changed your password!'})


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class DetailUpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class AccountLogoutView(LogoutView):
    permission_classes = (IsAuthenticated,)


class RefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
