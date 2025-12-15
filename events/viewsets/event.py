from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from events.models.event import Event
from events.serializers import (
    EventGetSerializer,
    EventCreateSerializer,
    EventUpdateSerializer,
    EventListSerializer,
)
from events.filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().select_related('department')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = EventFilter
    search_fields = ['title', 'department__name']
    ordering_fields = ['title', 'category', 'tag', 'amount', 'id']
    ordering = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        elif self.action == 'retrieve':
            return EventGetSerializer
        elif self.action == 'create':
            return EventCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return EventUpdateSerializer
        return EventGetSerializer
