"""
URL patterns for NetBox Software Plugin.

For more information on URL routing, see:
https://docs.netbox.dev/en/stable/plugins/development/views/#url-registration

For Django URL patterns, see:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    path("netbox-softwares/", views.NetboxsoftwareListView.as_view(), name="netboxsoftware_list"),
    path("netbox-softwares/add/", views.NetboxsoftwareEditView.as_view(), name="netboxsoftware_add"),
    path("netbox-softwares/<int:pk>/", views.NetboxsoftwareView.as_view(), name="netboxsoftware"),
    path("netbox-softwares/<int:pk>/edit/", views.NetboxsoftwareEditView.as_view(), name="netboxsoftware_edit"),
    path("netbox-softwares/<int:pk>/delete/", views.NetboxsoftwareDeleteView.as_view(), name="netboxsoftware_delete"),
    path(
        "netbox-softwares/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="netboxsoftware_changelog",
        kwargs={"model": models.Netboxsoftware},
    ),
)
