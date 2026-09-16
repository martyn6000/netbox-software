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
    # License Types
    path("license-types/", views.LicenseTypeListView.as_view(), name="licensetype_list"),
    path("license-types/add/", views.LicenseTypeEditView.as_view(), name="licensetype_add"),
    path("license-types/<int:pk>/", views.LicenseTypeView.as_view(), name="licensetype"),
    path("license-types/<int:pk>/edit/", views.LicenseTypeEditView.as_view(), name="licensetype_edit"),
    path("license-types/<int:pk>/delete/", views.LicenseTypeDeleteView.as_view(), name="licensetype_delete"),
    path(
        "license-types/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="licensetype_changelog",
        kwargs={"model": models.LicenseType},
    ),
    # Software Licenses
    path("software-licenses/", views.SoftwareLicenseListView.as_view(), name="softwarelicense_list"),
    path("software-licenses/add/", views.SoftwareLicenseEditView.as_view(), name="softwarelicense_add"),
    path("software-licenses/<int:pk>/", views.SoftwareLicenseView.as_view(), name="softwarelicense"),
    path("software-licenses/<int:pk>/edit/", views.SoftwareLicenseEditView.as_view(), name="softwarelicense_edit"),
    path(
        "software-licenses/<int:pk>/delete/",
        views.SoftwareLicenseDeleteView.as_view(),
        name="softwarelicense_delete",
    ),
    path(
        "software-licenses/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwarelicense_changelog",
        kwargs={"model": models.SoftwareLicense},
    ),
    # License Assignments
    path("license-assignments/", views.LicenseAssignmentListView.as_view(), name="licenseassignment_list"),
    path("license-assignments/add/", views.LicenseAssignmentEditView.as_view(), name="licenseassignment_add"),
    path("license-assignments/<int:pk>/", views.LicenseAssignmentView.as_view(), name="licenseassignment"),
    path(
        "license-assignments/<int:pk>/edit/",
        views.LicenseAssignmentEditView.as_view(),
        name="licenseassignment_edit",
    ),
    path(
        "license-assignments/<int:pk>/delete/",
        views.LicenseAssignmentDeleteView.as_view(),
        name="licenseassignment_delete",
    ),
    path(
        "license-assignments/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="licenseassignment_changelog",
        kwargs={"model": models.LicenseAssignment},
    ),
)
