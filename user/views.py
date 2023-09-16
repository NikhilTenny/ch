# Django imports
from common_services.helpers.response_structure import ResponseStructure
# Local imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user.services.users_services import UserServices
from user.serializers.users_serializers import UserSerializers

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








