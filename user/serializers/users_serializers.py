from rest_framework import serializers
from user.models import Users


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password']


