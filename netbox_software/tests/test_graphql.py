"""
Test cases for NetBox Software Plugin GraphQL API.
"""
from ..models import Netboxsoftware
from ..testing import PluginGraphQLTestCase


class NetboxsoftwareGraphQLTestCase(PluginGraphQLTestCase):
    """Test Netboxsoftware GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Netboxsoftware.objects.create(name='GraphQL Test 1')
        Netboxsoftware.objects.create(name='GraphQL Test 2')
        Netboxsoftware.objects.create(name='GraphQL Test 3')

    def test_query_netboxsoftware(self):
        """Test GraphQL query for a single Netboxsoftware."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        instance = Netboxsoftware.objects.first()

        query = (
            "query { "
            "netboxsoftware(id: " + str(instance.pk) + ") { "
            "id name "
            "} "
            "}"
        )

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['netboxsoftware']
        self.assertEqual(data['id'], str(instance.pk))
        self.assertEqual(data['name'], instance.name)

    def test_query_netboxsoftware_list(self):
        """Test GraphQL query for list of Netboxsoftwares."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        query = """
        query {
            netboxsoftware_list {
                id
                name
            }
        }
        """

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['netboxsoftware_list']
        self.assertEqual(len(data), 3)
        self.assertIn('id', data[0])
        self.assertIn('name', data[0])

    def test_query_netboxsoftware_with_all_fields(self):
        """Test GraphQL query with all available fields."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        instance = Netboxsoftware.objects.first()

        query = (
            "query { "
            "netboxsoftware(id: " + str(instance.pk) + ") { "
            "id name created last_updated "
            "} "
            "}"
        )

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['netboxsoftware']
        self.assertEqual(data['id'], str(instance.pk))
        self.assertEqual(data['name'], instance.name)
        self.assertIsNotNone(data['created'])
        self.assertIsNotNone(data['last_updated'])

