from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.reviews import ReviewsViewSet
from .views.comments import CommentsViewSet
from .views.users import MyUserViewSet

router = DefaultRouter()
# эндпоинты для работы с отзывами и комментариями
router.register(r'titles/(?P<title_id>[^/.]+)/reviews', ReviewsViewSet,
                basename='ReviewsView')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    CommentsViewSet, basename='CommentsView')
router.register(
    r'users', MyUserViewSet, basename='MyUserViewSet'
)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
