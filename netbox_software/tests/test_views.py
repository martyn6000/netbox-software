"""
Test cases for NetBox Software Plugin views.
"""

from django.urls import reverse

from ..models import Netboxsoftware
from ..testing import PluginViewTestCase
from ..testing.utils import disable_warnings, get_random_string


class NetboxsoftwareViewTestCase(PluginViewTestCase):
    """Test Netboxsoftware views."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Netboxsoftware.objects.create(name='View Test 1')
        Netboxsoftware.objects.create(name='View Test 2')
        Netboxsoftware.objects.create(name='View Test 3')

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.base_url = 'plugins:netbox_software:netboxsoftware'

    def test_list_netboxsoftwares(self):
        """Test Netboxsoftware list view."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        url = reverse('plugins:netbox_software:netboxsoftware_list')
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)

    def test_list_netboxsoftwares_without_permission(self):
        """Test Netboxsoftware list view without permission."""
        url = reverse('plugins:netbox_software:netboxsoftware_list')

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_view_netboxsoftware(self):
        """Test Netboxsoftware detail view."""
        self.add_permissions('netbox_software.view_netboxsoftware')

        instance = Netboxsoftware.objects.first()
        url = reverse('plugins:netbox_software:netboxsoftware', kwargs={'pk': instance.pk})
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)
        self.assertEqual(response.context['object'], instance)

    def test_create_netboxsoftware(self):
        """Test creating a Netboxsoftware via form."""
        self.add_permissions(
            'netbox_software.add_netboxsoftware',
            'netbox_software.view_netboxsoftware'
        )

        url = reverse('plugins:netbox_software:netboxsoftware_add')
        name = f'Created {get_random_string(10)}'

        form_data = self.post_data({
            'name': name,
        })

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was created
        instance = Netboxsoftware.objects.get(name=name)
        self.assertEqual(instance.name, name)

    def test_create_netboxsoftware_without_permission(self):
        """Test creating a Netboxsoftware without permission."""
        url = reverse('plugins:netbox_software:netboxsoftware_add')

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_edit_netboxsoftware(self):
        """Test editing a Netboxsoftware via form."""
        self.add_permissions(
            'netbox_software.change_netboxsoftware',
            'netbox_software.view_netboxsoftware'
        )

        instance = Netboxsoftware.objects.first()
        url = reverse('plugins:netbox_software:netboxsoftware_edit', kwargs={'pk': instance.pk})

        new_name = f'Edited {get_random_string(10)}'
        form_data = self.post_data({
            'name': new_name,
        })

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was updated
        instance.refresh_from_db()
        self.assertEqual(instance.name, new_name)

    def test_delete_netboxsoftware(self):
        """Test deleting a Netboxsoftware."""
        self.add_permissions(
            'netbox_software.delete_netboxsoftware',
            'netbox_software.view_netboxsoftware'
        )

        instance = Netboxsoftware.objects.first()
        url = reverse('plugins:netbox_software:netboxsoftware_delete', kwargs={'pk': instance.pk})

        # Confirm deletion
        response = self.client.post(url, {'confirm': True}, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was deleted
        self.assertFalse(
            Netboxsoftware.objects.filter(pk=instance.pk).exists()
        )

    def test_delete_netboxsoftware_without_permission(self):
        """Test deleting a Netboxsoftware without permission."""
        instance = Netboxsoftware.objects.first()
        url = reverse('plugins:netbox_software:netboxsoftware_delete', kwargs={'pk': instance.pk})

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)


class NetboxsoftwareFormTestCase(PluginViewTestCase):
    """Test Netboxsoftware form validation."""

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.add_permissions(
            'netbox_software.add_netboxsoftware',
            'netbox_software.view_netboxsoftware'
        )

    def test_form_validation_empty_name(self):
        """Test form validation with empty name."""
        url = reverse('plugins:netbox_software:netboxsoftware_add')
        form_data = self.post_data({'name': ''})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should not create object
        self.assertEqual(Netboxsoftware.objects.filter(name='').count(), 0)

    def test_form_validation_duplicate_name(self):
        """Test form validation with duplicate name."""
        Netboxsoftware.objects.create(name='Duplicate')

        url = reverse('plugins:netbox_software:netboxsoftware_add')
        form_data = self.post_data({'name': 'Duplicate'})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should only have one instance with this name
        self.assertEqual(Netboxsoftware.objects.filter(name='Duplicate').count(), 1)
