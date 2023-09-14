# Django imports
from common_services.helpers.response_structure import ResponseStructure
# Local imports
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import Users
from user.services.users_services import UserServices
from user.serializers.users_serializers import UserSerializers


class RegisterAPI(APIView):

    def post(self, request):
        try:
            request_body = request.data
            user_serializer = UserSerializers(data=request_body)

            if user_serializer.is_valid():
                user_data = user_serializer.validated_data
                user_service = UserServices()
                response = user_service.create_new_user(user_data)
                if response['success']:
                    return Response(response, status=200)
                else:
                    return Response(response, status=400)

            response = ResponseStructure.error_response(user_serializer.errors)
            return Response(response, status=400)

        except Exception as err:
            response = ResponseStructure.error_response(str(err))
            return Response(response, status=500)








