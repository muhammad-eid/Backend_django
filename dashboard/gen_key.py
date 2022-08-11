
from .models import Key
from random import randrange

def gen_unique_key():
    key = '1234-1234-1234-1234'
    if Key.objects.filter(key=key).exists():
        return randrange(1000, 99999999999999999999)
    else:
        return key

def gen_trail(user):
    Key(user=user, key=gen_unique_key(), type='Trail', duration=14).save()#change duration leater


def gen_gift(user):
    Key(user=user, key=gen_unique_key(), type='Gift', duration=90).save()


def gen_purchased(user):
    Key(user=user, key=gen_unique_key(), type='Purchased', duration=366, state='Suspended', is_active=False).save()