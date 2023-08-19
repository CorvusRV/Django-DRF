from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, SmsCode
from .serializers import CustomUserSerializer, SmsCodeSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


class CustomUserAPIView(APIView):
    """API для работы без указания номера пользователя"""

    def get(self, request):
        """при GET, выдает список всех зарегистрированных пользователей"""
        users = CustomUser.objects.all().values('id', 'phone', 'user_code', 'invite_code')
        return Response(users)

    def post(self, request):  # желательно большую часть логику перенести в serializers
        data = request.data  # получение данных из request
        phone = CustomUser.objects.filter(phone=data['phone']).exists()  # проверка на наличие пользователя с данным телефоном
        if phone is not True:  # если пользователя нет, то создается новый пользователь
            serializer = CustomUserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        # создание и отправка смс кода
        code = SmsCode.objects.filter(phone=data['phone']).exists()
        if code is True:  # Если код есть
            sms_active = SmsCode.objects.filter(phone=data['phone']).last()
            if sms_active.sms_active == False:
                code = data.get('code')
                if code is not None:
                    if data['code'] == str(sms_active.sms_code):
                        sms_active.sms_active = True
                        sms_active.save(update_fields=["sms_active"])
                        user = CustomUser.objects.filter(phone=data['phone']).last()
                        #return JsonResponse({'error': 'проверка'}, status=200)
                        token = Token.objects.get_or_create(user=user)  # токен не создается
                        return JsonResponse({'token': str(token)}, status=200)
                    else:
                        return Response({'error': 'код указан не верно'})
            else:
                SmsCode.objects.filter(phone=data['phone']).delete()
        sms_code = SmsCode.objects.create(phone=data['phone'])
        sms_code = SmsCodeSerializer(sms_code)
        return Response(sms_code.data)




class CustomUserDetailAPIView(APIView):
    """API для работы с конкретным пользователем, по его номеру"""
    # можно переделать на работу с номером телефона
    def get(self, request, pk):
        """при GET, с указанием номером, выдает данные о пользователе"""
        pk = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(pk)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        при PATCH, с укаанием номера, позволяет добавить инлайн код, если его нет
        иначе просто возвращает данные пользователя
        """
        pk = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(pk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)