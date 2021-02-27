from rest_framework import serializers

from ..models.users import MyUser#, UserRegistration


class MyUserSerializer(serializers.ModelSerializer):
    
    # def validate(self, date):
    #     if self.context['request'].user.is_admin:
    #         return date
    #     return self.instance.role

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

#     class Meta:
#         model = UserRegistration
#         fields = ['email', 'confirmation_code']
