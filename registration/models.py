import datetime
from django.db import models

from account.models import User

from django.utils import timezone############################


from .send_emails import send_return_otp
from datetime import timedelta



 
# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    activation_date = models.DateTimeField(auto_now_add=True)
    activation_code = models.CharField(max_length=8, blank=True, null=True)
    trys_num = models.IntegerField(default=0)
    # disable = models.BooleanField(default=False)
    ban = models.BooleanField(default=False)
    ban_date = models.DateTimeField(blank=True, null=True)


    # def generate_otp(self, user):
    #     confirmation = EmailConfirmation.create

    # def expired(self):
    #     now = timezone.now()
    #     return self.activation_date + datetime.timedelta(minutes=-1) <= self.activation_date <= now


    
    
    # # def confirm(self):
    # #     if self.activation_date.timedelta(minutes=5) <= timezone.now():
    # #         return self.activation_code

    # def generate(self, user, type='confirm'):
    #     activation_code = send_return_otp(type, user.email)
    #     Token(user=user, activation_code=activation_code).save()


    # def is_baned(self, request):
    #     user = User.objects.get(pk=request.user.id)
    #     if user.token.ban == True:
    #         if user.token.ban_date + timedelta(minutes=30) > timezone.now():
    #             context ={
    #                 'ban':user.token.ban_date + timedelta(minutes=30) - timezone.now()
    #             }
    #             return render(request, 'registration/email_verfiy.html', context) 
    #         else:
    #             user.token.ban == False
    #             user.token.trys_num = 0
    #             user.token.save()

    # def confirm(self):
    #     pass





