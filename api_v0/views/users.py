from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from ..permissions import IsAdmin

from ..models.users import MyUser, UserRegistration
from ..serializers.users import (
    MyUserSerializer,
    UserRegistrationSerializer,
    EmailSerializer,
)


@api_view(['POST'])
def registrations_request(request):
    serializer = EmailSerializer(data=request.data)
    if not serializer.is_valid():
        raise serializer.ValidationError(
            'You can\'tsubscribe to yourself.'
        )
    email = serializer.validated_data.get('email')
    confirmation_code = make_password('')
    UserRegistration.objects.create(
        email=email,
        confirmation_code=confirmation_code)
    return Response(serializer.data, )


@api_view(['POST'])
def get_token(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        raise serializers.ValidationError(
            'You can\'tsubscribe to yourself.'
        )
    email = serializer.validated_data.get('email')
    code = serializer.validated_data.get('confirmation_code')
    if UserRegistration.objects.filter(email=email,
                                       confirmation_code=code).exists():
        username = email.split('@')[0]
        user = MyUser.objects.create(email=email, username=username)
        code_registration = get_object_or_404(
            UserRegistration,
            email=email,
            confirmation_code=code
        )
        code_registration.delete()
        access_token = AccessToken.for_user(user)
        return Response({'token': f'{access_token}'})
    user = get_object_or_404(MyUser, email=email)
    access_token = AccessToken.for_user(user)
    return Response({'token': f'{access_token}'})


class MyUserViewSet (ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'username'
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user__username', ]
