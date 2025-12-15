from rest_framework import serializers
from events.models.ticket_pass import Pass


class PassGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['id', 'name', 'price', 'description', 'is_active']

class PassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['name', 'price', 'description', 'is_active']

class PassUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['name', 'price', 'description', 'is_active']
        extra_kwargs = {
            'name': {'required': False},
            'price': {'required': False},
            'description': {'required': False},
            'is_active': {'required': False},
        }

class PassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['id', 'name', 'price', 'description', 'is_active']
        read_only_fields = ['id']