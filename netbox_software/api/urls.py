"""
API URL patterns for NetBox Software Plugin.

For more information on NetBox REST API routing, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#routers

For Django REST Framework routers, see:
https://www.django-rest-framework.org/api-guide/routers/
"""

from netbox.api.routers import NetBoxRouter

from .views import LicenseAssignmentViewSet, LicenseTypeViewSet, SoftwareLicenseViewSet

app_name = "netbox_software"

router = NetBoxRouter()
router.register("license-types", LicenseTypeViewSet)
router.register("software-licenses", SoftwareLicenseViewSet)
router.register("license-assignments", LicenseAssignmentViewSet)

urlpatterns = router.urls
