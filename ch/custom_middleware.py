from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError

JWT_authenticator = JWTAuthentication()

from common_services.helpers.response_structure import ResponseStructure
from ch import settings

import logging
logger = logging.getLogger(__name__)


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authenticator = JWTAuthentication()

    def __call__(self, request):
        try:
            excluded_urls = settings.NO_AUTH_URLS
            if request.path_info in excluded_urls:
                return self.get_response(request)
            
            request_metadata = request.META
            if "HTTP_AUTHORIZATION" not in request_metadata:
                error_msg = "Authorization token not provided."
                self.return_error_response(error_msg, status.HTTP_400_BAD_REQUEST)
            
            user, token = self.jwt_authenticator.authenticate(request)
            return self.get_response(request)
        
        except InvalidToken as token_err:
            logger.error(repr(token_err))
            error_msg = "Invalid authorization token."
            self.return_error_response(error_msg, status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            logger.error(repr(err))
            self.return_error_response(repr(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def return_error_response(self, error_msg:str, status_code:int) -> Response:
        response_body = ResponseStructure.error_response(error_msg)
        response = Response(
                    data=response_body,
                    status=status_code)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response



        