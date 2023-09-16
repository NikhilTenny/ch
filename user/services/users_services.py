
from django.contrib.auth.hashers import make_password
from django.db import OperationalError

from common_services.helpers.response_structure import ServiceResponse
from user.models import Users
import logging


class UserServices:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def create_new_user(self, user_data: dict) -> ServiceResponse:
        """
            Creates a new user if user doesn't already exists.
        """

        try:
            existing_user =  Users.custom_obj.check_if_user_exists(user_data['email'])

            if existing_user is None:
                password_hash = make_password(user_data['password'])
                user_data['password'] = password_hash
                Users.objects.create(**user_data)
                response = ServiceResponse(
                    True, "User successfully created")
            else:
                response = ServiceResponse(
                    False, "Given email address already exists")
                
            return response
        except OperationalError as op_err:
            self.logger.error(str(op_err))
            response = ServiceResponse(False, "Something went wrong.")
            return response
        
        except Exception as err:
            self.logger.error(str(err))
            response = ServiceResponse(False, "Something went wrong.")
            return response