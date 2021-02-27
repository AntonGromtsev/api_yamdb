from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True)

    class RoleChoises(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        MODERATOR = 'moderator', _('Moderator')
        USER = 'user', _('User')

    role = CharField(
        max_length=50,
        choices=RoleChoises.choices,
        default=RoleChoises.USER.value,
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
