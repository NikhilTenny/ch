# Django imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login

# Local imports
from common_services.helpers.response_structure import ResponseStructure
from common_services.utilities.validations import Validation
from common_services.utilities.auth import JWTToken
from common_services.exceptions.common_exceptions import MissingRequiredFieldException
from user.services.users_services import UserServices
from user.serializers.users_serializers import UserSerializers
from user.models import Users

from rest_framework_simplejwt.tokens import RefreshToken

import logging
logger = logging.getLogger(__name__)


class RegisterAPI(APIView):

    def post(self, request):
        try:
            request_body = request.data
            user_service = UserServices()
            user_serializer = UserSerializers(data=request_body)

            if not user_serializer.is_valid():
                response = ResponseStructure.error_response(user_serializer.errors)
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            user_data = user_serializer.validated_data
            create_user_result = user_service.create_new_user(user_data)

            if create_user_result.success:
                response = ResponseStructure.success_msg_response(create_user_result.result)
                return Response(response, status=status.HTTP_201_CREATED)
            
            logger.error(create_user_result.result)
            response = ResponseStructure.error_response(create_user_result.result)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            logger.error(str(err))
            response = ResponseStructure.error_response("Something went wrong.")
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginAPI(APIView):

    def post(self, request):
        try:
            request_data = request.data
            required_fields = ['email', 'password']
            empty_or_missing_fields = Validation.validate_empty_or_missing_fields(
                request_data, required_fields)
            if empty_or_missing_fields:
                raise MissingRequiredFieldException(empty_or_missing_fields)
            
            user = authenticate(**request_data)
            if user is None:
                response = ResponseStructure.error_response("Invalid credentials")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            # Creating access and refresh tokens
            auth_tokens = JWTToken.get_tokens_for_user(user)

            response = ResponseStructure.success_response(auth_tokens, 'Login successful')
            return Response(response, status=status.HTTP_202_ACCEPTED)

            
        except MissingRequiredFieldException as field_error:
            logger.error(str(field_error))
            response = ResponseStructure.error_response(str(field_error))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            logger.error(str(err))
            response = ResponseStructure.error_response("Something went wrong.")
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







