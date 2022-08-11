from django.core.mail import send_mail

from random import randrange


def send_return_otp(type, receiver):
    activation_code = str(randrange(100,99999990)).zfill(8)
    if type=='confirm':
        send_mail(
            'Confirm Email on Estidama Software',
            'Confirm Email on Estidama Software, your OTP code is: '+ activation_code,
            'estidama@estidama-es.com',
            [receiver],
            fail_silently=False,################
        )
    if type=='reset':
        send_mail(
            'Reset password on Estidama Software',
            'Reset password on Estidama Software, your OTP code is: '+ activation_code,
            'estidama@estidama-es.com',
            [receiver],
            fail_silently=False,################
        )
    return activation_code


