"""
Views for NetBox Software Plugin.

For more information on NetBox views, see:
https://docs.netbox.dev/en/stable/plugins/development/views/

For generic view classes, see:
https://docs.netbox.dev/en/stable/development/views/
"""

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import filtersets, forms, models, tables
from .constants import CONTRACTS_INSTALLED


class LicenseTypeView(generic.ObjectView):
    queryset = models.LicenseType.objects.all()


class LicenseTypeListView(generic.ObjectListView):
    queryset = models.LicenseType.objects.all()
    table = tables.LicenseTypeTable
    filterset = filtersets.LicenseTypeFilterSet


class LicenseTypeEditView(generic.ObjectEditView):
    queryset = models.LicenseType.objects.all()
    form = forms.LicenseTypeForm


class LicenseTypeDeleteView(generic.ObjectDeleteView):
    queryset = models.LicenseType.objects.all()


class SoftwareLicenseView(generic.ObjectView):
    queryset = models.SoftwareLicense.objects.all()

    def get_extra_context(self, request, instance):
        return {"contracts_installed": CONTRACTS_INSTALLED}


class SoftwareLicenseListView(generic.ObjectListView):
    queryset = models.SoftwareLicense.objects.all()
    table = tables.SoftwareLicenseTable
    filterset = filtersets.SoftwareLicenseFilterSet


class SoftwareLicenseEditView(generic.ObjectEditView):
    queryset = models.SoftwareLicense.objects.all()
    form = forms.SoftwareLicenseForm


class SoftwareLicenseDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareLicense.objects.all()


class LicenseAssignmentView(generic.ObjectView):
    queryset = models.LicenseAssignment.objects.all()


class LicenseAssignmentListView(generic.ObjectListView):
    queryset = models.LicenseAssignment.objects.all()
    table = tables.LicenseAssignmentTable
    filterset = filtersets.LicenseAssignmentFilterSet


class LicenseAssignmentEditView(generic.ObjectEditView):
    queryset = models.LicenseAssignment.objects.all()
    form = forms.LicenseAssignmentForm


class LicenseAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = models.LicenseAssignment.objects.all()


# Optional integration: shows a "Contracts" tab on the Software License page when netbox_contracts is installed.
if apps.is_installed("netbox_contracts"):
    from netbox_contracts.filtersets import ContractAssignmentFilterSet
    from netbox_contracts.models import ContractAssignment
    from netbox_contracts.tables import ContractAssignmentObjectTable

    @register_model_view(models.SoftwareLicense, name="contracts", path="contracts")
    class SoftwareLicenseContractsView(generic.ObjectChildrenView):
        queryset = models.SoftwareLicense.objects.all()
        child_model = ContractAssignment
        table = ContractAssignmentObjectTable
        filterset = ContractAssignmentFilterSet
        template_name = "generic/object_children.html"
        tab = ViewTab(
            label="Contracts",
            badge=lambda obj: ContractAssignment.objects.filter(
                object_type=ContentType.objects.get_for_model(obj), object_id=obj.pk
            ).count(),
            permission="netbox_contracts.view_contractassignment",
        )

        def get_children(self, request, parent):
            return ContractAssignment.objects.filter(
                object_type=ContentType.objects.get_for_model(parent), object_id=parent.pk
            )
