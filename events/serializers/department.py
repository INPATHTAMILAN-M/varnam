from rest_framework import serializers
from events.models.department import Department


class DepartmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']
        read_only_fields = ['id']


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']
        read_only_fields = ['id']


class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'code']


class DepartmentPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'code']