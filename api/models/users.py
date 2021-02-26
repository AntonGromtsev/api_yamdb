from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, **kwargs):
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **kwargs)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, **kwargs):
#         list = {
#             'is_staff': True,
#             'is_superuser': True,
#         }
#         kwargs.update(list)
#         user = self.create_user(email, **kwargs)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True, blank=True)
    confirmation_code = models.CharField(max_length=254, blank=True)

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


class UserRegistration (models.Model):
    email = models.EmailField(max_length=254, unique=True)
    confirmation_code = models.CharField(max_length=254)
