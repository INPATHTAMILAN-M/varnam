from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from events.models.department import Department
from events.serializers import (
    DepartmentRetrieveSerializer,
    DepartmentListSerializer,
    DepartmentCreateSerializer,
    DepartmentPatchSerializer,
)
from events.filters import DepartmentFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = DepartmentFilter
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code', 'id']
    ordering = ['name']


    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentListSerializer
        elif self.action == 'retrieve':
            return DepartmentRetrieveSerializer
        elif self.action == 'create':
            return DepartmentCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return DepartmentPatchSerializer
        return DepartmentRetrieveSerializer


