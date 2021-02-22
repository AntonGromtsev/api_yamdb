from django.db import models

from .review import Review
from .users import MyUser


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарии',
        blank=True
    )
    text = models.CharField(max_length=255, verbose_name='Текст')
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return ': '.join([str(self.pub_date), self.review,
                          self.author, self.text[:15] + '...'])
