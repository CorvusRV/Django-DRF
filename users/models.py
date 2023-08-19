from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

import random

def generation_user_code():
    """функция генерирует 6 значный код из цифр и символов"""
    codes = [code['user_code'] for code in CustomUser.objects.all().values('user_code')]
    while True:
        gen_code = ''
        for i in range(6):
            gen_code += random.choice('+-/*!&$#?=@<>1234567890')
        if gen_code is not codes:
            return gen_code

def generation_sms_code():
    """функция генерирует 4 значный цифровой код"""
    return str(random.randint(1000, 9999))

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """класс для создания кастомного пользователя"""
    username = None
    email = None
    # добавить базовый пароль, равный zZ111111 для тестов,
    phone = models.CharField(max_length=20, unique=True, db_index=True)
    user_code = models.CharField(max_length=6, unique=True, db_index=True, default=generation_user_code)
    invite_code = models.CharField(max_length=6, default='')
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        """У пользователя есть конкретное разрешение?"""
        # базовый ответ, да
        return True

    def is_staff(self):
        """Есть ли у пользователя права админа?"""
        return self.staff

    @property
    def is_admin(self):
        """Является ли пользователь админом?"""
        return self.admin


class SmsCode(models.Model):
    """модель для хранения смс кодов"""
    phone = models.CharField(max_length=20, db_index=True)
    sms_code = models.IntegerField(default=generation_sms_code)
    sms_active = models.BooleanField(default=False)  # служит для проверки того, вводлся ли смс код
    created = models.DateTimeField(auto_now_add=True)  # служит для проверки, давности создания смс кода
    # длительность жизни кода не введена в функционал
