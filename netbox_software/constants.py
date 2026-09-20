from django.apps import apps

# The local currency field is only available when the netbox_contracts plugin is installed.
CONTRACTS_INSTALLED = apps.is_installed("netbox_contracts")
