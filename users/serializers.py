from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from .models import CustomUser, SmsCode

class CustomUserSerializer(ModelSerializer):
    invited_users = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'phone', 'user_code', 'invite_code', 'invited_users')

    def get_invited_users(self, obj):
        user_code = obj.user_code
        invited_users = CustomUser.objects.filter(invite_code=user_code).values_list('phone')
        invited_users = [phone[0] for phone in list(invited_users)]
        return invited_users

    def create(self, validated_data):
        """
        функция создание нового пользователя
        """
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        изменение данных пользователя
        можно поменять только инвайт код
        """
        if validated_data.get('invite_code') is not None:
            user_code = CustomUser.objects.exclude(phone=instance.phone).filter(
                user_code=validated_data['invite_code']).values_list('user_code')
            if instance.invite_code == '' and user_code != 0:
                instance.invite_code = validated_data.get("invite_code", instance.invite_code)
                instance.save()
                return instance
        return instance


class SmsCodeSerializer(ModelSerializer):

    class Meta:
        model = SmsCode
        fields = ["phone", "sms_code"]

    def create(self, validated_data):
        return SmsCode.objects.create(**validated_data)
