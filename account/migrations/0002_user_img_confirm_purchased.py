# Generated by Django 4.1 on 2022-08-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img_confirm_purchased',
            field=models.ImageField(blank=True, null=True, upload_to='images/confirmation/'),
        ),
    ]