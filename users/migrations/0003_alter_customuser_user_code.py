# Generated by Django 4.2.4 on 2023-08-18 03:55

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_code',
            field=models.CharField(db_index=True, default=users.models.generation_user_code, max_length=6, unique=True),
        ),
    ]
