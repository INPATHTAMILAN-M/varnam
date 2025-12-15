from rest_framework import serializers
from events.models import (
    Department,
    Event,
    Pass,
)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']
        read_only_fields = ['id']


class EventGetSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'category', 'tag', 'amount', 'department']
        read_only_fields = ['id']


class EventCreateSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Event
        fields = ['title', 'category', 'tag', 'amount', 'department_id']
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)


class EventUpdateSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Event
        fields = ['title', 'category', 'tag', 'amount', 'department_id']
        extra_kwargs = {
            'title': {'required': False},
            'category': {'required': False},
            'tag': {'required': False},
            'amount': {'required': False},
            'department_id': {'required': False},
        }


class EventListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'category', 'tag', 'amount', 'department']
        read_only_fields = ['id']
