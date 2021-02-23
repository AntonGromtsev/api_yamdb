from rest_framework import serializers

from ..models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        model = Review

    def validate(self, attrs):
        score = int(attrs.get('score'))
        if score < 1 or score > 10:
            raise serializers.ValidationError('Rating must be from 1 to 10.')
        if Review.objects.filter(
                title=self.context['view'].kwargs.get('title_id'),
                author=self.context['request']._user,
        ).exists() and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'You can write only one review to this title.'
            )
        return super(ReviewSerializer, self).validate(attrs)
