# Django imports
from common_services.helpers.response_structure import ResponseStructure
from django.http import HttpResponse
# Local imports
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import Users
from user.serializers.users_serializers import UserSerializers


class RegisterAPI(APIView):

    def post(self, request):
        try:
            request_body = request.data
            user_serializer = UserSerializers(data=request_body)
            if user_serializer.is_valid():
                user_obj = Users.objects.create(**user_serializer.data)
                response_data = UserSerializers(user_obj)
                response = ResponseStructure.success_response(
                    response_data.data, 
                    "User Created Successfully"
                )
                return Response(response, status=200)
            else:
                response = ResponseStructure.error_response(user_serializer.errors)
                return Response(response, status=400)

        except Exception as err:
            return HttpResponse(err)







