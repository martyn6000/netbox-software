"""
Search indexes for NetBox Software Plugin.

This module defines search indexes to make plugin models searchable in NetBox's
global search. See: https://docs.netbox.dev/en/stable/plugins/development/search/
"""

from netbox.search import SearchIndex

from .models import LicenseType, SoftwareLicense


class LicenseTypeIndex(SearchIndex):
    """Search index for LicenseType model."""

    model = LicenseType

    fields = (
        ("name", 100),
        ("description", 500),
    )

    display_attrs = (
        "description",
        "color",
    )


class SoftwareLicenseIndex(SearchIndex):
    """Search index for SoftwareLicense model."""

    model = SoftwareLicense

    fields = (
        ("license_name", 100),
        ("friendly_name", 200),
        ("license_sku", 50),
    )

    display_attrs = (
        "manufacturer",
        "license_type",
    )


# Register all search indexes for this plugin
# The PluginConfig will automatically load these indexes
indexes = (
    LicenseTypeIndex,
    SoftwareLicenseIndex,
)
