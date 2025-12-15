import django_filters
from events.models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Event title (contains)'
    )
    category = django_filters.ChoiceFilter(
        field_name='category',
        choices=Event.CATEGORY_CHOICES,
        label='Event category'
    )
    tag = django_filters.ChoiceFilter(
        field_name='tag',
        choices=Event.TAG_CHOICES,
        label='Event tag'
    )
    department = django_filters.NumberFilter(
        field_name='department__id',
        label='Department ID'
    )
    department_name = django_filters.CharFilter(
        field_name='department__name',
        lookup_expr='icontains',
        label='Department name (contains)'
    )
    amount_min = django_filters.NumberFilter(
        field_name='amount',
        lookup_expr='gte',
        label='Minimum amount'
    )
    amount_max = django_filters.NumberFilter(
        field_name='amount',
        lookup_expr='lte',
        label='Maximum amount'
    )
    
    class Meta:
        model = Event
        fields = ['title', 'category', 'tag', 'department', 'amount']
