"""
Tables for NetBox Software Plugin.

For more information on NetBox tables, see:
https://docs.netbox.dev/en/stable/plugins/development/tables/

For django-tables2 documentation, see:
https://django-tables2.readthedocs.io/
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .models import Netboxsoftware


class NetboxsoftwareTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Netboxsoftware
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
