from distutils.command import upload
from django.db import models
from account.models import User


# Create your models here.

#add gift to user model

# TYPE_CHOICES = [
#     ('P,', 'Purchased Version'),
#     ('G', 'Gift Version'),
#     ('T', 'Trail Version')
# ]
# STATE_CHOICE = [
#     ('R,', 'Running'),
#     ('S', 'Stopped'),
#     ('F', 'Expired'),
#     ('P', 'Waiting'),
#     ('P', 'Suspended'),
# ]

class Key(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    key     = models.CharField(max_length=19, unique=True)
    type    = models.CharField(max_length=10, default='Trail' )
    state   = models.CharField(max_length=12, default='Running')
    is_active  = models.BooleanField(default=True)###########
    duration = models.IntegerField(default=14)
    # img = models.ImageField(upload_to='images')
    # img = models.ImageField(upload_to='images/confirmation/', blank=True, null=True)
    img_confirm_purchased = models.ImageField(upload_to='images/confirmation/', blank=True, null=True)


    gen_date        = models.DateTimeField(auto_now_add=True)
    act_date        = models.DateTimeField(null=True, blank=True)
    last_check_date = models.DateTimeField(null=True, blank=True)

    user_name   = models.CharField(max_length=50, null=True, blank=True)
    uuid        = models.CharField(max_length=50, null=True, blank=True, unique=True)
    hddid       = models.CharField(max_length=50, null=True, blank=True, unique=True)
    mac_address = models.CharField(max_length=50, null=True, blank=True, unique=True)
    os_version  = models.CharField(max_length=50, null=True, blank=True)
    sw_version  = models.CharField(max_length=20, null=True, blank=True)

    reactivation_counts = models.IntegerField(default=0)

    # log = models.CharField(max_length=200, null=True,  blank=True)
    message = models.TextField(null=True, blank=True)
    notes   = models.TextField(null=True, blank=True)

    



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    header    = models.CharField(max_length=50, null=True, blank=True)
    body   = models.CharField(max_length=500, null=True, blank=True)



class GiftMessage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    body   = models.CharField(max_length=500, null=True, blank=True)

# class Settings(models.Model):
#     trail_duration = models.IntegerField(default=14)
#     gift_duration = models.IntegerField(default=90)
#     purchased_duration = models.IntegerField(default=366)