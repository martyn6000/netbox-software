"""
Test cases for NetBox Software Plugin GraphQL API.
"""

from dcim.models import Manufacturer, Site
from django.contrib.contenttypes.models import ContentType

from ..models import LicenseAssignment, LicenseType, SoftwareLicense
from ..testing import PluginGraphQLTestCase


class LicenseTypeGraphQLTestCase(PluginGraphQLTestCase):
    """Test LicenseType GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        LicenseType.objects.create(name="GraphQL Type 1")
        LicenseType.objects.create(name="GraphQL Type 2")
        LicenseType.objects.create(name="GraphQL Type 3")

    def test_query_license_type(self):
        self.add_permissions("netbox_software.view_licensetype")

        instance = LicenseType.objects.first()

        query = "query { license_type(id: " + str(instance.pk) + ") { id name } }"

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["license_type"]
        self.assertEqual(data["id"], str(instance.pk))
        self.assertEqual(data["name"], instance.name)

    def test_query_license_type_list(self):
        self.add_permissions("netbox_software.view_licensetype")

        query = """
        query {
            license_type_list {
                id
                name
            }
        }
        """

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["license_type_list"]
        self.assertEqual(len(data), 3)
        self.assertIn("id", data[0])
        self.assertIn("name", data[0])


class SoftwareLicenseGraphQLTestCase(PluginGraphQLTestCase):
    """Test SoftwareLicense GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        manufacturer = Manufacturer.objects.create(name="Acme Corp", slug="acme-corp")

        SoftwareLicense.objects.create(
            manufacturer=manufacturer,
            license_name="GraphQL License 1",
            license_sku="SKU-1",
        )
        SoftwareLicense.objects.create(
            manufacturer=manufacturer,
            license_name="GraphQL License 2",
            license_sku="SKU-2",
        )
        SoftwareLicense.objects.create(
            manufacturer=manufacturer,
            license_name="GraphQL License 3",
            license_sku="SKU-3",
        )

    def test_query_software_license(self):
        self.add_permissions("netbox_software.view_softwarelicense")

        instance = SoftwareLicense.objects.first()

        query = "query { software_license(id: " + str(instance.pk) + ") { id license_name license_sku } }"

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["software_license"]
        self.assertEqual(data["id"], str(instance.pk))
        self.assertEqual(data["license_name"], instance.license_name)

    def test_query_software_license_assignment_count(self):
        self.add_permissions("netbox_software.view_softwarelicense")

        instance = SoftwareLicense.objects.first()
        site_type = ContentType.objects.get_for_model(Site)
        site = Site.objects.create(name="Site 1", slug="site-1")
        LicenseAssignment.objects.create(software_license=instance, object_type=site_type, object_id=site.pk)

        query = "query { software_license(id: " + str(instance.pk) + ") { id assignment_count } }"

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["software_license"]
        self.assertEqual(data["assignment_count"], 1)

    def test_query_software_license_list(self):
        self.add_permissions("netbox_software.view_softwarelicense")

        query = """
        query {
            software_license_list {
                id
                license_name
            }
        }
        """

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["software_license_list"]
        self.assertEqual(len(data), 3)
        self.assertIn("id", data[0])
        self.assertIn("license_name", data[0])

    def test_query_software_license_with_all_fields(self):
        self.add_permissions("netbox_software.view_softwarelicense")

        instance = SoftwareLicense.objects.first()

        query = "query { software_license(id: " + str(instance.pk) + ") { id license_name created last_updated } }"

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["software_license"]
        self.assertEqual(data["id"], str(instance.pk))
        self.assertEqual(data["license_name"], instance.license_name)
        self.assertIsNotNone(data["created"])
        self.assertIsNotNone(data["last_updated"])


class LicenseAssignmentGraphQLTestCase(PluginGraphQLTestCase):
    """Test LicenseAssignment GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        manufacturer = Manufacturer.objects.create(name="Acme Corp", slug="acme-corp")
        software_license = SoftwareLicense.objects.create(
            manufacturer=manufacturer,
            license_name="GraphQL License",
            license_sku="SKU-1",
        )
        site_type = ContentType.objects.get_for_model(Site)
        site = Site.objects.create(name="Site 1", slug="site-1")

        LicenseAssignment.objects.create(
            software_license=software_license,
            object_type=site_type,
            object_id=site.pk,
        )

    def test_query_license_assignment(self):
        self.add_permissions("netbox_software.view_licenseassignment")

        instance = LicenseAssignment.objects.first()

        query = "query { license_assignment(id: " + str(instance.pk) + ") { id object_id software_license { id } } }"

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["license_assignment"]
        self.assertEqual(data["id"], str(instance.pk))
        self.assertEqual(data["object_id"], instance.object_id)

    def test_query_license_assignment_list(self):
        self.add_permissions("netbox_software.view_licenseassignment")

        query = """
        query {
            license_assignment_list {
                id
                object_id
            }
        }
        """

        response = self.execute_query(query)
        self.assertIsNone(response.get("errors"))

        data = response["data"]["license_assignment_list"]
        self.assertEqual(len(data), 1)
        self.assertIn("id", data[0])
