from rest_framework import serializers

from ..models.users import User


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()
