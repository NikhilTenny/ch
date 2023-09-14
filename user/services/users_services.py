
from django.contrib.auth.hashers import make_password

from common_services.helpers.response_structure import ResponseStructure
from user.models import Users
                                                                                                


class UserServices:
    
    def create_new_user(self, user_data) -> ResponseStructure:
        """
            Creates a new user if user doesn't already exists.
        """
        try:
            user_exists = Users.custom_obj.check_if_user_exists(user_data['email'])

            if not user_exists:
                password_hash = make_password(user_data['password'])
                user_data['password'] = password_hash
                Users.objects.create(**user_data)
                response = ResponseStructure.success_msg_response(
                    "User successfully created"
                )
            else:
                response = ResponseStructure.error_response(
                    "Given email address already exists"
                )

            return response
        
        except Exception:
            response = ResponseStructure.error_response("Something went wrong.")
            return response