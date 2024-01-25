from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action

from Todo.utils import response_fun, get_tokens_for_user
from accounts.models import User
from accounts.serializers import RegistrationSerializer, UserLoginSerializer


class AccountViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def register(self, request):
        data = request.data
        email = data.get('email', None)
        if email is None:
            return response_fun(0, "Email Not Found")

        is_email_exists = User.objects.filter(pk=email).exists()
        if is_email_exists:
            return response_fun(0, "Email already exists")

        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response_fun(1, "Registration Successful")
        else:
            return response_fun(0, str(serializer.errors))

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return response_fun(0, "Email or password Not Found")
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            User.objects.filter(pk=user.pk).update(last_login=timezone.now())
            return response_fun(1, {'token': token, 'msg': 'Login Successful'})
        else:
            return response_fun(0, 'Email or Password is not Valid')
