"""
NetBox Software Plugin

Plugin configuration for NetBox Software Plugin.

For a complete list of PluginConfig attributes, see:
https://docs.netbox.dev/en/stable/plugins/development/#pluginconfig-attributes
"""

__author__ = """Martyn Stanton"""
__email__ = "martynstanton@hotmail.com"
__version__ = "1.0"


from netbox.plugins import PluginConfig


class NetboxsoftwareConfig(PluginConfig):
    name = "netbox_software"
    verbose_name = "NetBox Software Plugin"
    description = "NetBox plugin for netbox-software."
    author= "Martyn Stanton"
    author_email = "martynstanton@hotmail.com"
    version = __version__
    base_url = "netbox_software"
    min_version = "4.5.0"
    max_version = "4.5.99"
    graphql_schema = "graphql.schema"


config = NetboxsoftwareConfig
