from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReviewsViewSet, CommentsViewSet

router = DefaultRouter()
# эндпоинты для работы с отзывами и комментариями
router.register(r'titles/(?P<title_id>[^/.]+)/reviews', ReviewsViewSet,
                basename='ReviewsView')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    CommentsViewSet, basename='CommentsView')

urlpatterns = [
    path('', include(router.urls)),
]
