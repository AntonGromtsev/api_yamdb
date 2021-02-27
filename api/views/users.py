from re import S
from django.db.models import query
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView

from ..permissions import IsAdmin, IsAuthorOrReadOnly
from ..models.users import MyUser#, UserRegistration
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
    #serializer = EmailSerializer(data=request.data)
    email = serializer.validated_data.get('email')
    code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(MyUser, email=email)
    if default_token_generator.check_token(user, code):
        access_token = AccessToken.for_user(user)
        return Response({'token': f'{access_token}'})
    return Response({'token': 'Invalid authorization token'})


class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'username'
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user__username', ]


class MyUserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = MyUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = MyUserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
