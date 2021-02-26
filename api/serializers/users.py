from rest_framework import serializers

from ..models.users import MyUser, UserRegistration


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role'
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', )


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = UserRegistration
        fields = ['email', 'confirmation_code', ]
