from rest_framework import serializers
from varnam.models.event import Event
from varnam.serializers.department import DepartmentSerializer


class EventSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Event
        fields = ['id', 'department', 'department_id', 'title', 'category', 'tag', 'amount']
    
    def create(self, validated_data):
        department_id = validated_data.pop('department_id', None)
        if department_id:
            validated_data['department_id'] = department_id
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        department_id = validated_data.pop('department_id', None)
        if department_id:
            validated_data['department_id'] = department_id
        return super().update(instance, validated_data)
