from rest_framework import viewsets, filters, status, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from ..models.categories import Category
from ..serializers.categories import CategorySerializer
from ..permissions import IsAdminOrReadOnly


class CreateCategoryViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                             mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateCategoryViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
