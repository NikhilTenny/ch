
class ResponseStructure:

    @staticmethod
    def success_response(payload, message:str) -> dict:
        """ Return successfull API response"""
        return {
            'success': True,
            'data': payload,
            'message': message
        }
    
    @staticmethod
    def error_response(error:str) -> dict:
        """ Return error API response"""
        return {
            'success': False,
            'data': None,
            'message': error
        }