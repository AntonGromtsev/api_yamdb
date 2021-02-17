from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .titles import Titles
from .users import User


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        verbose_name='Произведение',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=1023, verbose_name='Текст')
    author = models.ForeignKey(
        User,
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

    def __str__(self):
        return ': '.join(
            [str(self.pub_date), self.author, self.text[:15] + '...'])
