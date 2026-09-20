"""
Navigation menu items for NetBox Software Plugin.

For more information on navigation menus, see:
https://docs.netbox.dev/en/stable/plugins/development/navigation/
"""

from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

softwarelicense_buttons = [
    PluginMenuButton(
        link="plugins:netbox_software:softwarelicense_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

licensetype_buttons = [
    PluginMenuButton(
        link="plugins:netbox_software:licensetype_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

licenseassignment_buttons = [
    PluginMenuButton(
        link="plugins:netbox_software:licenseassignment_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu = PluginMenu(
    label="Software",
    icon_class="mdi mdi-application-cog-outline",
    groups=(
        (
            "Software",
            (
                PluginMenuItem(
                    link="plugins:netbox_software:softwarelicense_list",
                    link_text="Software Licenses",
                    buttons=softwarelicense_buttons,
                ),
                PluginMenuItem(
                    link="plugins:netbox_software:licenseassignment_list",
                    link_text="License Assignments",
                    buttons=licenseassignment_buttons,
                ),
                PluginMenuItem(
                    link="plugins:netbox_software:licensetype_list",
                    link_text="License Types",
                    buttons=licensetype_buttons,
                ),
            ),
        ),
    ),
)
