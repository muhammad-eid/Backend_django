# Generated by Django 4.1 on 2022-08-11 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_key_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='img',
        ),
    ]