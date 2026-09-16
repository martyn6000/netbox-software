"""
Views for NetBox Software Plugin.

For more information on NetBox views, see:
https://docs.netbox.dev/en/stable/plugins/development/views/

For generic view classes, see:
https://docs.netbox.dev/en/stable/development/views/
"""

from netbox.views import generic

from . import filtersets, forms, models, tables


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
