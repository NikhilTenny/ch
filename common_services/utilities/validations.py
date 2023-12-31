from common_services.exceptions.common_exceptions import MissingRequiredFieldException

from typing import Union, List

class Validation:

    @staticmethod
    def validate_empty_or_missing_fields(request_data: dict, required_fields: list)-> Union[List[str], bool]:
        """
        Validate that the required fields are not 
        missing or empty in the given request.
        """
        missing_or_empty_fields = []
        for field in required_fields:
            if field not in request_data or request_data[field] == "":
                missing_or_empty_fields.append(field)
        if missing_or_empty_fields:
            raise MissingRequiredFieldException(missing_or_empty_fields)
        
    @staticmethod
    def format_serializer_errors(serializer_errors):
        field_names = {}
        for field_name, field_errors in serializer_errors.items():
            field_names[field_name] = str(field_errors[0])
        return field_names