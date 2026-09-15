"""
API URL patterns for NetBox Software Plugin.

For more information on NetBox REST API routing, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#routers

For Django REST Framework routers, see:
https://www.django-rest-framework.org/api-guide/routers/
"""

from netbox.api.routers import NetBoxRouter

from .views import NetboxsoftwareViewSet

app_name = "netbox_software"

router = NetBoxRouter()
router.register("netbox-softwares", NetboxsoftwareViewSet)

urlpatterns = router.urls

