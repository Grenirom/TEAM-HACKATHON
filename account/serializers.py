from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name', 'username')

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs.pop('password2')
        if password2 != password:
            raise serializers.ValidationError('Passwords didn\'t match!')
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, email):
        user = get_object_or_404(User, email=email)
        if not user.is_active:
            raise serializers.ValidationError("User account is not active.")
        return email

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.reset_code = uuid4().hex
        user.save()
        return user


class ConfirmResetSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)


    def validate(self, attrs):
        password = attrs['password']
        password_confirm = attrs['password_confirm']
        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        reset_code = self.context['reset_code']
        user = User.objects.get(reset_code=reset_code)

        # Установите новый пароль для пользователя
        password = validated_data['password']
        user.set_password(password)
        user.reset_code = ''
        user.save()
        return user

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_superuser', 'is_staff', 'date_joined', 'activation_code',
                   'groups', 'user_permissions')


# class ChangePasswordSerializer(serializers.Serializer):
#     model = User
#
#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
