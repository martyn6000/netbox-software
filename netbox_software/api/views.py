"""
API viewsets for NetBox Software Plugin.

For more information on NetBox REST API viewsets, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#viewsets

For Django REST Framework viewsets, see:
https://www.django-rest-framework.org/api-guide/viewsets/
"""

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets
from ..models import LicenseAssignment, LicenseType, SoftwareLicense
from .serializers import LicenseAssignmentSerializer, LicenseTypeSerializer, SoftwareLicenseSerializer


class LicenseTypeViewSet(NetBoxModelViewSet):
    queryset = LicenseType.objects.all()
    serializer_class = LicenseTypeSerializer
    filterset_class = filtersets.LicenseTypeFilterSet


class SoftwareLicenseViewSet(NetBoxModelViewSet):
    queryset = SoftwareLicense.objects.all()
    serializer_class = SoftwareLicenseSerializer
    filterset_class = filtersets.SoftwareLicenseFilterSet


class LicenseAssignmentViewSet(NetBoxModelViewSet):
    queryset = LicenseAssignment.objects.all()
    serializer_class = LicenseAssignmentSerializer
    filterset_class = filtersets.LicenseAssignmentFilterSet
