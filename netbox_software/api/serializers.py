"""
API serializers for NetBox Software Plugin.

Serializers are required for NetBox event handling (webhooks, change logging).
They also power the REST API endpoints.

For more information on NetBox REST API serializers, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#serializers

For Django REST Framework serializers, see:
https://www.django-rest-framework.org/api-guide/serializers/
"""

from dcim.api.serializers import ManufacturerSerializer
from django.contrib.contenttypes.models import ContentType
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from netbox.api.fields import ContentTypeField
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers
from utilities.api import get_serializer_for_model

from ..constants import CONTRACTS_INSTALLED
from ..models import LicenseAssignment, LicenseType, SoftwareLicense


class LicenseTypeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_software-api:licensetype-detail")

    class Meta:
        model = LicenseType
        fields = (
            "id",
            "url",
            "display",
            "name",
            "description",
            "color",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "url", "display", "name", "description", "color")


class SoftwareLicenseSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_software-api:softwarelicense-detail")
    manufacturer = ManufacturerSerializer(nested=True, required=True, allow_null=False)
    license_type = LicenseTypeSerializer(nested=True, required=False, allow_null=True)
    assignment_count = serializers.IntegerField(read_only=True)
    if CONTRACTS_INSTALLED:
        from netbox_contracts.api.serializers import CurrencySerializer

        local_currency = CurrencySerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = SoftwareLicense
        fields = (
            "id",
            "url",
            "display",
            "manufacturer",
            "license_name",
            "friendly_name",
            "license_sku",
            "per_license_cost",
            *(("local_currency",) if CONTRACTS_INSTALLED else ()),
            "license_type",
            "assignment_count",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "url", "display", "license_name", "friendly_name", "license_sku")


class LicenseAssignmentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_software-api:licenseassignment-detail")
    software_license = SoftwareLicenseSerializer(nested=True)
    object_type = ContentTypeField(queryset=ContentType.objects.all())
    assigned_object = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LicenseAssignment
        fields = (
            "id",
            "url",
            "display",
            "software_license",
            "object_type",
            "object_id",
            "assigned_object",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "url", "display")

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_assigned_object(self, instance):
        if instance.assigned_object is None:
            return None
        serializer = get_serializer_for_model(instance.assigned_object)
        context = {"request": self.context["request"]}
        return serializer(instance.assigned_object, nested=True, context=context).data
