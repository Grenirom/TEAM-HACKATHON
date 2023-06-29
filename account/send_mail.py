from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

HOST = '127.0.0.1:8000'

User = get_user_model()


def send_activation_code(user, code):
    link = f'http://{HOST}/account/activate/{code}'
    send_mail(
        'Здравствуйте!',
        'Для активации вашего аккаунта, необходимо перейти по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка действительна только 1 раз!',
        'ngrebnev17@gmail.com',
        [user],
        fail_silently=False
    )


def create_activation_code(self):
    code = str(uuid4())
    User.objects.get(activation_code=code)
    print(code, '========================')


def send_password_change_mail(user):
    code = str(uuid4())
    print(code, '=============')
    link = f'http://{HOST}/account/reset/confirm_reset/{code}'
    send_mail(
        'Здравствуйте!',
        'Для сброса пароля, перейдите по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка действительна только 1 раз!',
        'ngrebnev17@gmail.com',
        [user],
        fail_silently=False
    )
