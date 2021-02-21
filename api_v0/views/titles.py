from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status, permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from ..models.titles import Title
from ..serializers.titles import TitleSerializer
from ..permissions import IsAuthorOrReadOnly
#всё ещё не понимаю, почему здесь проверка на автора, а не на админа
from ..filters.filters import TitlesFilter


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter
