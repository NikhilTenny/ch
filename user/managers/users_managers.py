from django.db import models
from django.utils.translation import gettext_lazy as _

class UsersManager(models.Manager):
    
    def check_if_user_exists(self, email):
        """ Checks if the user already exists"""
        if not email:
            raise ValueError(_("The Email must be set"))
        try:
            user = self.get(email=email)
            return user
        except self.model.DoesNotExist:
            return None
