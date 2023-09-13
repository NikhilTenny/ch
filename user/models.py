from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from user.managers.users_managers import UsersManager

class Users(AbstractUser):
    phone_number = PhoneNumberField()

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
    


    



