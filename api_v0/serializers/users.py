from rest_framework import serializers
from ..models.users import MyUser


class MyUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role', )
