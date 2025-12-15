from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from varnam.models.department import Department
from varnam.serializers.department import DepartmentSerializer
from varnam.filters.department import DepartmentFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = DepartmentFilter
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code', 'id']
    ordering = ['name']
