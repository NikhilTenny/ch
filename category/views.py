import logging

from common_services.utilities.validations import Validation
from common_services.helpers.response_structure import ResponseStructure
from category.serializers.user_category_serializer import UserCategorySerializer
from category.services.user_category_services import UserCategoryService
from category.models import UserCategory

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class UserCategoryAPI(APIView):
    user_category_service = UserCategoryService()

    def post(self, request):
        try:
            request_data = request.data
            request_data["user_id"] = request.META['user']['id']
            status_code, serializer = self.user_category_service.get_serialized_data(request_data)
            if 400 <= status_code <= 599:
                response = ResponseStructure.error_response(serializer)
                return Response(response, status_code)
            
            create_data = self.user_category_service.create_and_retrive_record(serializer)
            response = ResponseStructure.success_response(
                    create_data, "New records created successfully."
                    )
            return Response(response, status.HTTP_201_CREATED)

        except Exception as error:
            logger.error(repr(error))
            response = ResponseStructure.error_response("Something went wrong.")
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)