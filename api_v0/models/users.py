from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields import CharField


class MyUserManager(BaseUserManager):

    def create_user(self, email):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, **kwargs):
        user = self.create_user(email, )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    ROLE_CHOISES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    role = CharField(max_length=50, choices=ROLE_CHOISES, default='user')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
