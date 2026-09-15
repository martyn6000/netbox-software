"""
Views for NetBox Software Plugin.

For more information on NetBox views, see:
https://docs.netbox.dev/en/stable/plugins/development/views/

For generic view classes, see:
https://docs.netbox.dev/en/stable/development/views/
"""

from netbox.views import generic

from . import filtersets, forms, models, tables


class NetboxsoftwareView(generic.ObjectView):
    queryset = models.Netboxsoftware.objects.all()


class NetboxsoftwareListView(generic.ObjectListView):
    queryset = models.Netboxsoftware.objects.all()
    table = tables.NetboxsoftwareTable
    filterset = filtersets.NetboxsoftwareFilterSet


class NetboxsoftwareEditView(generic.ObjectEditView):
    queryset = models.Netboxsoftware.objects.all()
    form = forms.NetboxsoftwareForm


class NetboxsoftwareDeleteView(generic.ObjectDeleteView):
    queryset = models.Netboxsoftware.objects.all()
