from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import random


class UserManager(BaseUserManager):
    def create_user(self, phone, password):
        """Создайте и сохраните пользователя с указанным номером телефона."""
        if not phone:
            raise ValueError(_('Номер телеона не введен'))
        user = self.model(phone=phone)
        user.user_code = self.generator_code()
        #user.set_password(password)
        user.set_password('zZ111Zz')
        user.save()
        return user

    def create_superuser(self, phone, password):
        """Создайте и сохраните суперпользователя с указанным номером телефона и паролем."""
        if password is None:
            raise TypeError('Суперпользователи должны иметь пароль.')
        user = self.create_user(phone, password)
        user.user_code = self.generator_code()
        user.is_superuser = True
        user.staff = True
        user.save()
        return user

    def get_full_name(self):
        """Возвращает first_name плюс last_name с пробелом между ними"""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Возвращает короткое имя пользователя"""
        return self.first_name

    def generator_code(self):
        code = ''
        for i in range(6):
            code += random.choice('+-/*!&$#?=@<>1234567890')
        return code