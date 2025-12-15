from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from varnam.models.event import Event
from varnam.serializers.event import EventSerializer
from varnam.filters.event import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().select_related('department')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = EventFilter
    search_fields = ['title', 'department__name']
    ordering_fields = ['title', 'category', 'tag', 'amount', 'id']
    ordering = ['title']
