from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):

    def _create_user(self, email, **kwargs):
        if not email:
            raise ValueError(_('The Email must be set')))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, **kwargs):
        return self._create_user(self, email, is_superuser=False)

    def create_superuser(self, email, **kwargs):
        return self._create_user(self, email, ,is_staff=True, is_superuser=True)





class User(models.Model):
    pass
