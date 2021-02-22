from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .titles import Title
from .users import MyUser


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        related_name='reviews',
        on_delete=models.CASCADE,
        blank=True,
    )
    text = models.CharField(max_length=1023,
                            verbose_name='Текст',
                            null=False)
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(10)],
        verbose_name='Рейтинг'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-pub_date',)
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['author', 'title'],
        #         name='unique_review'
        #     ),
        # ]

    # def __str__(self):
    #     return ': '.join(
    #         [str(self.pub_date), self.author, self.text[:15] + '...'])
