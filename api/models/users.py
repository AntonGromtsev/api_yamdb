from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


class RoleChoises(models.TextChoices):
        ADMIN = 'admin'
        MODERATOR = 'moderator'
        USER = 'user'


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

    role = CharField(
        max_length=50,
        choices=RoleChoises.choices,
        default=RoleChoises.USER,
        verbose_name='Роль пользователя',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    @property
    def is_moderator(self):
        return self.role == RoleChoises.MODERATOR

    @property
    def is_admin(self):
        return (
            self.role == RoleChoises.ADMIN
            or self.is_staff
            or self.is_superuser
        )

    def __str__(self):
        return self.email #!!!!

User = get_user_model()