from rest_framework import serializers

from ..models.users import MyUser


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'username')


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()
