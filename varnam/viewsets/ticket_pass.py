from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from varnam.models.ticket_pass import Pass
from varnam.serializers.ticket_pass import PassSerializer
from varnam.filters.ticket_pass import PassFilter


class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = PassFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'is_active', 'id']
    ordering = ['name']
