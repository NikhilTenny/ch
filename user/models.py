from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

from user.managers.users_managers import UsersManager

from phonenumber_field.modelfields import PhoneNumberField

class Users(AbstractUser):
    phone_number = PhoneNumberField()
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    username = None
    REQUIRED_FIELDS = []
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_user_user_permissions'
    )

    objects = UsersManager()

    def __str__(self):
        return self.email
