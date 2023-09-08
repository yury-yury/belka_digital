from rest_framework import serializers

from main.models import OreSample
from users.serializers import UserSerializer


class OreSampleCreateSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = OreSample
        fields = "__all__"


class OreSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OreSample
        fields = ("iron_content", "silicon_content", "aluminum_content", "calcium_content", "sulfur_content")

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     for field in ["iron_content", "silicon_content", "aluminum_content", "calcium_content","sulfur_content"]:
    #         representation[field] = self.context[field]
    #
    #     return representation
