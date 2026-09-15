"""
API viewsets for NetBox Software Plugin.

For more information on NetBox REST API viewsets, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#viewsets

For Django REST Framework viewsets, see:
https://www.django-rest-framework.org/api-guide/viewsets/
"""

from netbox.api.viewsets import NetBoxModelViewSet

from ..models import Netboxsoftware
from .serializers import NetboxsoftwareSerializer


class NetboxsoftwareViewSet(NetBoxModelViewSet):
    queryset = Netboxsoftware.objects.all()
    serializer_class = NetboxsoftwareSerializer

