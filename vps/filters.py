from django_filters import rest_framework as filters

from .models import VPS


class VPSFilter(filters.FilterSet):
    cpu = filters.NumberFilter(field_name="cpu", lookup_expr="exact")
    cpu__gt = filters.NumberFilter(field_name="cpu", lookup_expr="gt")
    cpu__gte = filters.NumberFilter(field_name="cpu", lookup_expr="gte")
    cpu__lt = filters.NumberFilter(field_name="cpu", lookup_expr="lt")
    cpu__lte = filters.NumberFilter(field_name="cpu", lookup_expr="lte")

    ram = filters.NumberFilter(field_name="ram", lookup_expr="exact")
    ram__gt = filters.NumberFilter(field_name="ram", lookup_expr="gt")
    ram__gte = filters.NumberFilter(field_name="ram", lookup_expr="gte")
    ram__lt = filters.NumberFilter(field_name="ram", lookup_expr="lt")
    ram__lte = filters.NumberFilter(field_name="ram", lookup_expr="lte")

    hdd = filters.NumberFilter(field_name="hdd", lookup_expr="exact")
    hdd__gt = filters.NumberFilter(field_name="hdd", lookup_expr="gt")
    hdd__gte = filters.NumberFilter(field_name="hdd", lookup_expr="gte")
    hdd__lt = filters.NumberFilter(field_name="hdd", lookup_expr="lt")
    hdd__lte = filters.NumberFilter(field_name="hdd", lookup_expr="lte")

    class Meta:
        model = VPS
        fields = ("cpu", "ram", "hdd",)
