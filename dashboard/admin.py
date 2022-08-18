from django.contrib import admin

from .models import Key, Notification, GiftMessage
# Register your models here.

admin.site.register(Key)
admin.site.register(Notification)
admin.site.register(GiftMessage)



