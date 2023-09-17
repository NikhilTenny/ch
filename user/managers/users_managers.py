from django.contrib.auth.models import BaseUserManager
from django.db import OperationalError
from django.utils.translation import gettext_lazy as _

class UsersManager(BaseUserManager):
    
    def check_if_user_exists(self, email: str):
        """ Checks if the user already exists"""
        try:
            if not email:
                raise ValueError(_("The Email must be set"))
            user = self.get(email=email)
            return user
        
        except self.model.DoesNotExist: # User does not exist
            return None
        
        except OperationalError as op_error:
            raise OperationalError(
                f"Database Operation error: {op_error}"
            ) from op_error
        
        except Exception as err:
            raise Exception(f"Error occured: {str(err)}") from err