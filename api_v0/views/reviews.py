from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..models.review import Review
from ..models.titles import Title
from ..models.users import MyUser
from ..permissions import IsAuthorOrReadOnly
from ..serializers.reviews import ReviewSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        
        serializer.save(author=self.request.user, title=title)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid()
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
    #     text = request.data.get('text')
    #     score = request.data.get('score')
    #     if not text or not score:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)
    #     author = get_object_or_404(MyUser, pk=request.user.id)
    #     review_count = title.reviews.filter(author=author).count()
    #     if review_count:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)
    #     review = title.reviews.create(
    #         text=text,
    #         score=score,
    #         author=author
    #     )
    #     serializer = ReviewSerializer(review)
    #     id = Review.objects.last()
    #     serializer.data['id'] = id
    #     serializer.validate(request.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
