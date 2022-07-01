from .models import Link
from rest_framework import serializers

class LinkSerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Link
        fields = '__all__'