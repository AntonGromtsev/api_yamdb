from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from ..permissions import IsAdmin
from ..models.users import MyUser
from ..serializers.users import (
    MyUserSerializer,
    UserRegistrationSerializer,
    EmailSerializer,
)

from api_yamdb.settings import EMAIL_HOST_USER


def send_msg(email, code):
    subject = 'Response with code confirmation'
    body = f'''
        {code}
    '''
    send_mail(
        subject, body,
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True
    )


@api_view(['POST'])
def registrations_request(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    username = serializer.validated_data.get('username')
    user = MyUser.objects.create(
        email=email,
        username=username,
    )
    confirmation_code = default_token_generator.make_token(user)
    send_msg(email, confirmation_code)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(MyUser, email=email)
    if default_token_generator.check_token(user, code):
        access_token = AccessToken.for_user(user)
        return Response(
            {'token': f'{access_token}'},
            status=status.HTTP_200_OK,
        )
    return Response(
        {'token': 'Invalid authorization token'},
        status=status.HTTP_400_BAD_REQUEST,
    )


class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'username'
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user__username']

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        if request.method == 'GET':
            return Response(
                self.serializer_class(request.user).data,
                status=status.HTTP_200_OK,
            )
        serializer = self.serializer_class(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        if not serializer.validated_data.get('role') or request.user.is_admin:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise serializers.ValidationError(
            'You don\'t have enough rights to change the user role.'
        )
