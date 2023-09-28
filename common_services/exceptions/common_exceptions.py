
class MissingRequiredFieldException(Exception):
    def __init__(self, missing_fields):
        self.missing_fields = missing_fields
        super().__init__(f"Errors in the following fields: {missing_fields}")