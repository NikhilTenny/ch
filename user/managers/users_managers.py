from django.db import models
from django.db import OperationalError
from django.utils.translation import gettext_lazy as _
from common_services.exceptions.user_exceptions import UserNotFoundException

class UsersManager(models.Manager):
    
    def check_if_user_exists(self, email: str):
        """ Checks if the user already exists"""
        # TODO:
        # 1. Add login in exceptions
        try:
            if not email:
                raise ValueError(_("The Email must be set"))
            user = self.get(email=email)
            return user
        
        except self.model.DoesNotExist:
            return None
        
        except OperationalError as op_error:
            raise OperationalError(
                f"Database Operation error: {op_error}"
            ) from op_error
        
        except Exception as err:
            raise Exception(f"Error occured: {str(err)}") from err