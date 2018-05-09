from .models import CompanyListing
import django_filters


class LocationFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CompanyListing

        fields = [
            'location',
        ]