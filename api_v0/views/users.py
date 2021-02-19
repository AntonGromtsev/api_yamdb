from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ..models.users import MyUser
from ..serializers.users import MyUserSerializer


class MyUserViewSet (ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
