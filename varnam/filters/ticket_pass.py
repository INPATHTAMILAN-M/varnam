import django_filters
from varnam.models.ticket_pass import Pass


class PassFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Pass name (contains)'
    )
    is_active = django_filters.BooleanFilter(
        field_name='is_active',
        label='Is active'
    )
    price_min = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Minimum price'
    )
    price_max = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Maximum price'
    )
    
    class Meta:
        model = Pass
        fields = ['name', 'is_active', 'price']
