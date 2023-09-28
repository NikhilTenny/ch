from rest_framework import serializers
from user.models import Users


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = Users
        fields = ['id','email', 'first_name', 'last_name', 'phone_number', 'password']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Exclude the "password" field from the serialized data
        data.pop('password', None)
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=128) 


