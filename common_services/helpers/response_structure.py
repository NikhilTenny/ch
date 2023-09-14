
class ResponseStructure:

    @staticmethod
    def success_response(payload, message:str) -> dict:
        """ Return successfull API response
            containing payload and message
        """
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
    
    @staticmethod
    def success_msg_response(message:str) -> dict:
        """ Return successfull API response 
            containing message
        """
        return {
            'success': True,
            'data': None,
            'message': message
        }