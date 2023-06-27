from django.core.mail import send_mail

HOST = '127.0.0.1:8000'


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