from rest_framework import viewsets

from ..models.review import Review
from ..permissions import IsAuthorOrReadOnly
from ..serializers.reviews import ReviewSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]
    # filter_class = ReviewFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
