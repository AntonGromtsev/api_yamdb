from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields import CharField


class MyUserManager(BaseUserManager):
    def create_user(self, email, **kwargs):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, **kwargs):
        user = self.create_user(email, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, blank=True)
    ROLE_CHOISES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    role = CharField(max_length=50, choices=ROLE_CHOISES, default='user')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email
