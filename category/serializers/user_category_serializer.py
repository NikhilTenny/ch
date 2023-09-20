from rest_framework import serializers

from category.models import UserCategory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCategory
        fields = ["id", "name", "parent_id", "main_category_id", "user_id"]