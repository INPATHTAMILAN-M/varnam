from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from events.models.ticket_pass import Pass
from events.serializers.ticket_pass import (
    PassGetSerializer,
    PassCreateSerializer,
    PassUpdateSerializer,
    PassListSerializer,
)
from events.filters import PassFilter


class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = PassFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'is_active', 'id']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return PassListSerializer
        elif self.action == 'retrieve':
            return PassGetSerializer
        elif self.action == 'create':
            return PassCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return PassUpdateSerializer
        return PassGetSerializer


