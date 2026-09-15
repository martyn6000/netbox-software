"""
Test cases for NetBox Software Plugin models.
"""

from django.core.exceptions import ValidationError

from ..models import Netboxsoftware
from ..testing import PluginModelTestCase
from ..testing.utils import create_tags, get_random_string


class NetboxsoftwareTestCase(PluginModelTestCase):
    """Test Netboxsoftware model."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        # Create test instances
        Netboxsoftware.objects.create(name='Test 1')
        Netboxsoftware.objects.create(name='Test 2')
        Netboxsoftware.objects.create(name='Test 3')

    def test_create_netboxsoftware(self):
        """Test creating a Netboxsoftware instance."""
        name = f'Test {get_random_string(10)}'
        instance = Netboxsoftware.objects.create(name=name)

        self.assertEqual(instance.name, name)
        self.assertIsNotNone(instance.pk)

    def test_netboxsoftware_str(self):
        """Test Netboxsoftware string representation."""
        instance = Netboxsoftware.objects.first()
        self.assertEqual(str(instance), instance.name)

    def test_netboxsoftware_absolute_url(self):
        """Test Netboxsoftware get_absolute_url method."""
        instance = Netboxsoftware.objects.first()
        url = instance.get_absolute_url()

        self.assertIsNotNone(url)
        self.assertIn(str(instance.pk), url)

    def test_netboxsoftware_unique_name(self):
        """Test that Netboxsoftware names must be unique."""
        name = 'Duplicate Name'
        Netboxsoftware.objects.create(name=name)

        with self.assertRaises(ValidationError):
            instance = Netboxsoftware(name=name)
            instance.full_clean()

    def test_model_to_dict(self):
        """Test model_to_dict helper method."""
        instance = Netboxsoftware.objects.first()
        data = self.model_to_dict(instance)

        self.assertIn('name', data)
        self.assertEqual(data['name'], instance.name)
        self.assertIn('id', data)

    def test_instance_equal(self):
        """Test assertInstanceEqual helper method."""
        instance = Netboxsoftware.objects.first()

        # Should pass with matching data
        self.assertInstanceEqual(
            instance,
            {'name': instance.name, 'id': instance.pk}
        )

    def test_netboxsoftware_with_tags(self):
        """Test Netboxsoftware with tags."""
        tags = create_tags(['important', 'test'])
        instance = Netboxsoftware.objects.first()

        instance.tags.add(*tags)
        instance.save()

        self.assertEqual(instance.tags.count(), 2)
        self.assertIn(tags[0], instance.tags.all())

    def test_bulk_create(self):
        """Test bulk creation of Netboxsoftware instances."""
        initial_count = Netboxsoftware.objects.count()

        instances = [
            Netboxsoftware(name=f'Bulk {i}')
            for i in range(5)
        ]
        Netboxsoftware.objects.bulk_create(instances)

        self.assertEqual(
            Netboxsoftware.objects.count(),
            initial_count + 5
        )

    def test_query_filter(self):
        """Test filtering Netboxsoftware instances."""
        # Create a specific instance for filtering
        test_name = f'FilterTest {get_random_string(10)}'
        Netboxsoftware.objects.create(name=test_name)

        # Test filter
        results = Netboxsoftware.objects.filter(name=test_name)
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().name, test_name)

    def test_ordering(self):
        """Test Netboxsoftware default ordering."""
        instances = list(Netboxsoftware.objects.all())

        # Check that instances are ordered by name
        names = [instance.name for instance in instances]
        self.assertEqual(names, sorted(names))


class NetboxsoftwareValidationTestCase(PluginModelTestCase):
    """Test Netboxsoftware validation."""

    def test_empty_name(self):
        """Test that empty name is not allowed."""
        with self.assertRaises(ValidationError):
            instance = Netboxsoftware(name='')
            instance.full_clean()

    def test_name_max_length(self):
        """Test name field max length."""
        long_name = 'x' * 101  # Exceeds max_length of 100

        with self.assertRaises(ValidationError):
            instance = Netboxsoftware(name=long_name)
            instance.full_clean()
