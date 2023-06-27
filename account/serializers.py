from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Если пользователь с указанным адресом электронной почты не найден
                return render(request, 'password_reset.html', {'form': form, 'error': 'User not found'})

            token = default_token_generator.make_token(user)  # Генерация и сохранение токена сброса пароля
            user.password_reset_token = token
            user.save()

            # Отправка письма с инструкциями по сбросу пароля
            reset_link = request.build_absolute_uri(f'/password-reset/{token}')
            send_mail(
                'Password Reset',
                f'Please follow the link to reset your password: {reset_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

            return render(request, 'password_reset.html', {'form': form, 'success': True})
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})


def password_reset_confirm(request, token):
    try:
        user = User.objects.get(password_reset_token=token)
    except User.DoesNotExist:
        return render(request, 'password_reset_confirm.html', {'error': 'Invalid or expired token'})
    # Если токен недействителен или истек

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:

            user.set_password(password)
            user.password_reset_token = ''  # Изменение пароля пользователя
            user.save()
            return render(request, 'password_reset_confirm.html', {'success': True})
        else:
            return render(request, 'password_reset_confirm.html', {'error': 'Passwords do not match'})

    return render(request, 'password_reset_confirm.html')
