from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import PageNumberPagination

from ..models.categories import Category
from ..serializers.categories import CategorySerializer
from ..permissions import IsAdminOrReadOnly


class MixinViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    pass


class CategoryViewSet(MixinViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
