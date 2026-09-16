"""
Filtersets for NetBox Software Plugin.

For more information on NetBox filtersets, see:
https://docs.netbox.dev/en/stable/plugins/development/filtersets/

For django-filters documentation, see:
https://django-filter.readthedocs.io/
"""

import django_filters
from dcim.models import Manufacturer
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import ContentTypeFilter

from .models import LicenseAssignment, LicenseType, SoftwareLicense


class LicenseTypeFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = LicenseType
        fields = ("id", "name", "description", "color")

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))


class SoftwareLicenseFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label="Manufacturer (ID)",
    )
    license_type_id = django_filters.ModelMultipleChoiceFilter(
        queryset=LicenseType.objects.all(),
        label="License Type (ID)",
    )

    class Meta:
        model = SoftwareLicense
        fields = (
            "id",
            "license_name",
            "friendly_name",
            "license_sku",
            "manufacturer_id",
            "license_type_id",
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(license_name__icontains=value) | Q(friendly_name__icontains=value) | Q(license_sku__icontains=value)
        )


class LicenseAssignmentFilterSet(NetBoxModelFilterSet):
    software_license_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SoftwareLicense.objects.all(),
        label="Software License (ID)",
    )
    object_type = ContentTypeFilter()

    class Meta:
        model = LicenseAssignment
        fields = ("id", "software_license_id", "object_type_id", "object_id")

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(software_license__license_name__icontains=value) | Q(software_license__license_sku__icontains=value)
        )
