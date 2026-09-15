"""
Forms for NetBox Software Plugin.

For more information on NetBox forms, see:
https://docs.netbox.dev/en/stable/plugins/development/forms/
"""

from netbox.forms import NetBoxModelForm

from .models import Netboxsoftware


class NetboxsoftwareForm(NetBoxModelForm):
    class Meta:
        model = Netboxsoftware
        fields = ("name", "tags")
