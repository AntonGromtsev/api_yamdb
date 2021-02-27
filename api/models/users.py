from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Фамилия',
    )
    bio = models.TextField(blank=True, verbose_name='Биография')
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта',
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Имя пользователя',
    )

    class RoleChoises(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        MODERATOR = 'moderator', _('Moderator')
        USER = 'user', _('User')

    role = CharField(
        max_length=50,
        choices=RoleChoises.choices,
        default=RoleChoises.USER.value,
        verbose_name='Роль пользователя',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    @property
    def is_moderator(self):
        return self.role == self.RoleChoises.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.RoleChoises.ADMIN

    def __str__(self):
        return self.email
