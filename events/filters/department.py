import django_filters
from events.models import Department


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Department name (contains)'
    )
    code = django_filters.CharFilter(
        field_name='code',
        lookup_expr='iexact',
        label='Department code (exact)'
    )
    
    class Meta:
        model = Department
        fields = ['name', 'code']
