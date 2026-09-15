"""
Test cases for NetBox Software Plugin REST API.
"""
from ..models import Netboxsoftware
from ..testing import PluginAPITestCase
from ..testing.utils import disable_warnings, get_random_string


class NetboxsoftwareAPITestCase(PluginAPITestCase):
    """Test Netboxsoftware API endpoints."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Netboxsoftware.objects.create(name='API Test 1')
        Netboxsoftware.objects.create(name='API Test 2')
        Netboxsoftware.objects.create(name='API Test 3')

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.list_url_name = 'plugins-api:netbox_software-api:netboxsoftware-list'
        self.detail_url_name = 'plugins-api:netbox_software-api:netboxsoftware-detail'

    def test_list_netboxsoftwares(self):
        """Test GET request to list Netboxsoftwares."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        url = self._get_list_url()
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)
        self.assertEqual(response.data['count'], 3)
        self.assertIn('results', response.data)

    def test_list_netboxsoftwares_without_permission(self):
        """Test GET request without permission."""
        url = self._get_list_url()

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_get_netboxsoftware(self):
        """Test GET request for a single Netboxsoftware."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        instance = Netboxsoftware.objects.first()
        url = self._get_detail_url(instance)
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)
        self.assertEqual(response.data['id'], instance.pk)
        self.assertEqual(response.data['name'], instance.name)

    def test_create_netboxsoftware(self):
        """Test POST request to create a Netboxsoftware."""
        self.add_permissions('netbox_software.add_netboxsoftware')

        url = self._get_list_url()
        name = f'API Created {get_random_string(10)}'

        data = {
            'name': name,
        }

        response = self.client.post(url, data, format='json')
        self.assertHttpStatus(response, 201)

        # Verify object was created
        instance = Netboxsoftware.objects.get(name=name)
        self.assertEqual(instance.name, name)
        self.assertEqual(response.data['id'], instance.pk)

    def test_create_netboxsoftware_without_permission(self):
        """Test POST request without permission."""
        url = self._get_list_url()

        with disable_warnings('django.request'):
            response = self.client.post(url, {'name': 'Test'}, format='json')
            self.assertHttpStatus(response, 403)

    def test_bulk_create_netboxsoftwares(self):
        """Test bulk creation via API."""
        self.add_permissions('netbox_software.add_netboxsoftware')

        url = self._get_list_url()
        data = [
            {'name': f'Bulk {i}'} for i in range(1, 4)
        ]

        response = self.client.post(url, data, format='json')
        self.assertHttpStatus(response, 201)
        self.assertEqual(len(response.data), 3)

        # Verify objects were created
        for item in data:
            self.assertTrue(
                Netboxsoftware.objects.filter(name=item['name']).exists()
            )

    def test_update_netboxsoftware(self):
        """Test PATCH request to update a Netboxsoftware."""
        self.add_permissions('netbox_software.change_netboxsoftware')

        instance = Netboxsoftware.objects.first()
        url = self._get_detail_url(instance)
        new_name = f'Updated {get_random_string(10)}'

        data = {'name': new_name}

        response = self.client.patch(url, data, format='json')
        self.assertHttpStatus(response, 200)

        # Verify object was updated
        instance.refresh_from_db()
        self.assertEqual(instance.name, new_name)

    def test_update_netboxsoftware_without_permission(self):
        """Test PATCH request without permission."""
        instance = Netboxsoftware.objects.first()
        url = self._get_detail_url(instance)

        with disable_warnings('django.request'):
            response = self.client.patch(url, {'name': 'Test'}, format='json')
            self.assertHttpStatus(response, 403)

    def test_delete_netboxsoftware(self):
        """Test DELETE request to remove a Netboxsoftware."""
        self.add_permissions('netbox_software.delete_netboxsoftware')

        instance = Netboxsoftware.objects.first()
        url = self._get_detail_url(instance)

        response = self.client.delete(url)
        self.assertHttpStatus(response, 204)

        # Verify object was deleted
        self.assertFalse(
            Netboxsoftware.objects.filter(pk=instance.pk).exists()
        )

    def test_delete_netboxsoftware_without_permission(self):
        """Test DELETE request without permission."""
        instance = Netboxsoftware.objects.first()
        url = self._get_detail_url(instance)

        with disable_warnings('django.request'):
            response = self.client.delete(url)
            self.assertHttpStatus(response, 403)

    def test_options_netboxsoftware(self):
        """Test OPTIONS request for list endpoint."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        url = self._get_list_url()
        response = self.client.options(url)

        self.assertHttpStatus(response, 200)


class NetboxsoftwareAPIValidationTestCase(PluginAPITestCase):
    """Test Netboxsoftware API validation."""

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.add_permissions('netbox_software.add_netboxsoftware')
        self.list_url_name = 'plugins-api:netbox_software-api:netboxsoftware-list'

    def test_create_with_empty_name(self):
        """Test that API validates empty name."""
        url = self._get_list_url()
        data = {'name': ''}

        response = self.client.post(url, data, format='json')
        self.assertHttpStatus(response, 400)
        self.assertIn('name', response.data)

    def test_create_with_duplicate_name(self):
        """Test that API validates duplicate names."""
        Netboxsoftware.objects.create(name='Duplicate')

        url = self._get_list_url()
        data = {'name': 'Duplicate'}

        response = self.client.post(url, data, format='json')
        self.assertHttpStatus(response, 400)

    def test_create_with_missing_required_field(self):
        """Test that API validates required fields."""
        url = self._get_list_url()
        data = {}  # Missing name

        response = self.client.post(url, data, format='json')
        self.assertHttpStatus(response, 400)
        self.assertIn('name', response.data)

