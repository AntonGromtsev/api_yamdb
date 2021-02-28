from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .titles import Title
from .users import User


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='reviews',
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='Произведение',
    )
    text = models.TextField(verbose_name='Текст',
                            null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        verbose_name='Рейтинг',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return ': '.join(
            [str(self.pub_date), self.author, self.text[:15] + '...'])
