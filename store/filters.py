import django_filters
from django_filters import CharFilter

from store.models import Product


class ProductFilter(django_filters.FilterSet):

    search_by_name = CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Product
        fields = []

