# Generated by Django 4.2.4 on 2023-08-18 20:40

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_user_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=20)),
                ('sms_code', models.IntegerField(default=users.models.generation_sms_code)),
                ('sms_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
