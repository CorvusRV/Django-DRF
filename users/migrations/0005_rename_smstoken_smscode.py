# Generated by Django 4.2.4 on 2023-08-19 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_smstoken'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SmsToken',
            new_name='SmsCode',
        ),
    ]
