"""
Tables for NetBox Software Plugin.

For more information on NetBox tables, see:
https://docs.netbox.dev/en/stable/plugins/development/tables/

For django-tables2 documentation, see:
https://django-tables2.readthedocs.io/
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import LicenseAssignment, LicenseType, SoftwareLicense


class LicenseTypeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    color = columns.ColorColumn()

    class Meta(NetBoxTable.Meta):
        model = LicenseType
        fields = ("pk", "id", "name", "description", "color", "actions")
        default_columns = ("name", "description", "color")


class SoftwareLicenseTable(NetBoxTable):
    license_name = tables.Column(linkify=True)
    manufacturer = tables.Column(linkify=True)
    license_type = tables.Column(linkify=True)
    assignment_count = columns.LinkedCountColumn(
        viewname="plugins:netbox_software:licenseassignment_list",
        url_params={"software_license_id": "pk"},
        verbose_name="Assigned Licenses",
        orderable=False,
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwareLicense
        fields = (
            "pk",
            "id",
            "manufacturer",
            "license_name",
            "friendly_name",
            "license_sku",
            "per_license_cost",
            "license_type",
            "assignment_count",
            "actions",
        )
        default_columns = (
            "manufacturer",
            "license_name",
            "friendly_name",
            "license_sku",
            "per_license_cost",
            "license_type",
            "assignment_count",
        )


class LicenseAssignmentTable(NetBoxTable):
    software_license = tables.Column(linkify=True)
    object_type = columns.ContentTypeColumn(verbose_name="Object Type")
    assigned_object = tables.Column(
        verbose_name="Object",
        linkify=True,
        orderable=False,
    )

    class Meta(NetBoxTable.Meta):
        model = LicenseAssignment
        fields = ("pk", "id", "software_license", "object_type", "assigned_object", "actions")
        default_columns = ("software_license", "object_type", "assigned_object")
