from rest_framework import serializers
from varnam.models.ticket_pass import Pass


class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['id', 'name', 'price', 'description', 'is_active']
