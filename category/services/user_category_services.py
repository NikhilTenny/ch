import logging

from rest_framework import status

from common_services.exceptions.common_exceptions import \
    MissingRequiredFieldException
from category.serializers.user_category_serializer import UserCategorySerializer
from common_services.exceptions.common_exceptions import MissingRequiredFieldException
from common_services.utilities.validations import Validation
from common_services.helpers.response_structure import ServiceResponse

logger = logging.getLogger(__name__)

class UserCategoryService:
    def __init__(self):
        self.serializer = UserCategorySerializer

    def get_serialized_data(self, req_data:dict) -> ServiceResponse :
        """
            Returns serailizer with data after serialization and validation
        """
        try:
            serializer_instance = self.serializer(data=req_data)
            if not serializer_instance.is_valid():
                serializer_errors = Validation.format_serializer_errors(serializer_instance.errors)
                raise MissingRequiredFieldException(serializer_errors)
            return status.HTTP_200_OK, serializer_instance
        
        except MissingRequiredFieldException as field_error:
            logger.error(repr(field_error))
            return status.HTTP_400_BAD_REQUEST, str(field_error)
        except Exception as err:
            logger.error(repr(err))
            return status.HTTP_400_BAD_REQUEST, str(err)
    
    def create_and_retrive_record(self, serializer):
        """
        Create a record and returns the data in the newly created record.
        """
        record_instance = serializer.save()
        deserialized_data = self.serializer(record_instance).data
        return deserialized_data