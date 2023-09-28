import logging

# Local imports
from common_services.exceptions.common_exceptions import \
    MissingRequiredFieldException
from common_services.helpers.response_structure import ResponseStructure
from common_services.utilities.auth import JWTToken
from common_services.utilities.validations import Validation

# Django imports
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers.users_serializers import UserSerializers, LoginSerializer
from user.services.users_services import UserServices

logger = logging.getLogger(__name__)


class RegisterAPI(APIView):
    user_service = UserServices()

    def post(self, request):
        try:
            request_body = request.data
            user_serializer = UserSerializers(data=request_body)

            if not user_serializer.is_valid():
                response = ResponseStructure.error_response(user_serializer.errors)
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            user_data = user_serializer.validated_data
            create_user_result = self.user_service.create_new_user(user_data)

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
            login_serializer = LoginSerializer(data=request_data)
            
            if not login_serializer.is_valid():
                validation_errors = Validation.format_serializer_errors(login_serializer.errors)
                raise MissingRequiredFieldException(validation_errors)
            user = authenticate(**request_data)
            if user is None:
                response = ResponseStructure.error_response("Invalid credentials")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            # Creating access and refresh tokens
            auth_tokens = JWTToken.get_tokens_for_user(user)

            logger.info(f"{user.email} logged in successfully.")
            response = ResponseStructure.success_response(auth_tokens, "Login successfull")
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except MissingRequiredFieldException as field_error:
            logger.error(str(field_error))
            response = ResponseStructure.error_response(str(field_error))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            logger.error(str(err))
            response = ResponseStructure.error_response("Something went wrong.")
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







