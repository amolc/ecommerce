import json
from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from organisations.models import Organisation
from .models import Category
from .serializers import CategorySerializer


class CategoryModelTest(TestCase):
    """Test cases for Category model"""

    def setUp(self):
        """Set up test data"""
        self.organisation = Organisation.objects.create(
            name="Test Organisation",
            display_name="Test Organisation Display"
        )
        
        self.category = Category.objects.create(
            category_name="Electronics",
            category_description="Electronic devices and accessories",
            is_active=True,
            organisation=self.organisation
        )

    def test_category_creation(self):
        """Test that a category can be created"""
        self.assertEqual(self.category.category_name, "Electronics")
        self.assertEqual(self.category.category_description, "Electronic devices and accessories")
        self.assertTrue(self.category.is_active)
        self.assertEqual(self.category.organisation, self.organisation)

    def test_category_string_representation(self):
        """Test the string representation of category"""
        self.assertEqual(str(self.category), "Electronics")

    def test_category_meta_verbose_name(self):
        """Test the verbose name plural"""
        self.assertEqual(Category._meta.verbose_name_plural, 'product_categories')

    def test_category_unique_name(self):
        """Test that category names are unique"""
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Electronics",  # Same name
                organisation=self.organisation
            )

    def test_category_default_values(self):
        """Test default values for category"""
        category = Category.objects.create(
            category_name="Test Category",
            organisation=self.organisation
        )
        self.assertTrue(category.is_active)
        self.assertIsNotNone(category.created_at)
        self.assertIsNotNone(category.updated_at)


class CategorySerializerTest(TestCase):
    """Test cases for Category serializer"""

    def setUp(self):
        """Set up test data"""
        self.organisation = Organisation.objects.create(
            name="Test Organisation",
            display_name="Test Organisation Display"
        )
        
        self.category_data = {
            'category_name': 'Books',
            'category_description': 'Books and literature',
            'is_active': True,
            'category_image': 'books.jpg',
            'organisation': self.organisation.id
        }
        
        self.category = Category.objects.create(
            category_name="Electronics",
            category_description="Electronic devices and accessories",
            is_active=True,
            organisation=self.organisation
        )

    def test_category_serializer_valid_data(self):
        """Test serializer with valid data"""
        serializer = CategorySerializer(data=self.category_data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
        self.assertTrue(serializer.is_valid())

    def test_category_serializer_invalid_data(self):
        """Test serializer with invalid data"""
        invalid_data = self.category_data.copy()
        invalid_data['category_name'] = ''  # Empty name
        serializer = CategorySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('category_name', serializer.errors)

    def test_category_serializer_serialization(self):
        """Test serialization of category instance"""
        serializer = CategorySerializer(self.category)
        data = serializer.data
        self.assertEqual(data['category_name'], 'Electronics')
        self.assertEqual(data['category_description'], 'Electronic devices and accessories')
        self.assertTrue(data['is_active'])

    def test_category_serializer_update(self):
        """Test updating category through serializer"""
        update_data = {
            'category_name': 'Electronics Updated',
            'category_description': 'Updated description'
        }
        serializer = CategorySerializer(self.category, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_category = serializer.save()
        self.assertEqual(updated_category.category_name, 'Electronics Updated')


class CategoryAPITest(APITestCase):
    """Test cases for Category API endpoints"""

    def setUp(self):
        """Set up test data"""
        # Create test organisation
        self.organisation = Organisation.objects.create(
            name="Test Organisation",
            display_name="Test Organisation Display"
        )
        
        # Create test category
        self.category = Category.objects.create(
            category_name="Electronics",
            category_description="Electronic devices and accessories",
            is_active=True,
            organisation=self.organisation
        )
        
        # Set up API client (no authentication needed)
        self.client = APIClient()

    def test_list_categories(self):
        """Test listing all categories"""
        url = '/1/api/category/categories/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['category_name'], 'Electronics')

    def test_list_categories_with_filter(self):
        """Test listing categories with filters"""
        # Create another category
        Category.objects.create(
            category_name="Clothing",
            category_description="Clothing and accessories",
            is_active=False,
            organisation=self.organisation
        )
        
        # Test filter by is_active
        url = '/1/api/category/categories/?is_active=true'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['category_name'], 'Electronics')

    def test_create_category(self):
        """Test creating a new category"""
        url = '/1/api/category/categories/'
        data = {
            'category_name': 'Books',
            'category_description': 'Books and literature',
            'is_active': True,
            'organisation': self.organisation.id
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['category_name'], 'Books')
        
        # Verify category was created in database
        self.assertTrue(Category.objects.filter(category_name='Books').exists())

    def test_create_category_invalid_data(self):
        """Test creating category with invalid data"""
        url = '/1/api/category/categories/'
        data = {
            'category_name': '',  # Empty name
            'organisation': self.organisation.id
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')

    def test_create_category_duplicate_name(self):
        """Test creating category with duplicate name"""
        url = '/1/api/category/categories/'
        data = {
            'category_name': 'Electronics',  # Same name as existing
            'organisation': self.organisation.id
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')

    def test_retrieve_category(self):
        """Test retrieving a specific category"""
        url = f'/1/api/category/categories/{self.category.id}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['category_name'], 'Electronics')

    def test_retrieve_category_not_found(self):
        """Test retrieving non-existent category"""
        url = '/1/api/category/categories/999/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category_full(self):
        """Test full update of category"""
        url = f'/1/api/category/categories/{self.category.id}/'
        data = {
            'category_name': 'Electronics Updated',
            'category_description': 'Updated description',
            'is_active': False,
            'organisation': self.organisation.id
        }
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['category_name'], 'Electronics Updated')
        self.assertFalse(response.data['data']['is_active'])

    def test_update_category_partial(self):
        """Test partial update of category"""
        url = f'/1/api/category/categories/{self.category.id}/'
        data = {
            'category_name': 'Electronics Updated'
        }
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['category_name'], 'Electronics Updated')
        # Other fields should remain unchanged
        self.assertEqual(response.data['data']['category_description'], 'Electronic devices and accessories')

    def test_delete_category(self):
        """Test deleting a category"""
        url = f'/1/api/category/categories/{self.category.id}/'
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['status'], 'success')
        
        # Verify category was deleted from database
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

    def test_delete_category_not_found(self):
        """Test deleting non-existent category"""
        url = '/1/api/category/categories/999/'
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_active_categories(self):
        """Test listing only active categories"""
        # Create inactive category
        Category.objects.create(
            category_name="Inactive Category",
            is_active=False,
            organisation=self.organisation
        )
        
        url = '/1/api/category/categories/active/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        # Should only return active categories
        for category in response.data['data']:
            self.assertTrue(category['is_active'])

    def test_toggle_category_status(self):
        """Test toggling category status"""
        url = f'/1/api/category/categories/{self.category.id}/toggle_status/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertFalse(response.data['data']['is_active'])
        
        # Toggle again
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['data']['is_active'])

    def test_toggle_category_status_not_found(self):
        """Test toggling status of non-existent category"""
        url = '/1/api/category/categories/999/toggle_status/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_public_access(self):
        """Test that API is publicly accessible"""
        # Create client without authentication
        client = APIClient()
        url = '/1/api/category/categories/'
        response = client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryIntegrationTest(TestCase):
    """Integration tests for Category functionality"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.organisation = Organisation.objects.create(
            name="Test Organisation",
            display_name="Test Organisation Display"
        )

    def test_category_workflow(self):
        """Test complete category workflow"""
        # 1. Create category
        category = Category.objects.create(
            category_name="Test Category",
            category_description="Test description",
            is_active=True,
            organisation=self.organisation
        )
        
        # 2. Verify creation
        self.assertEqual(category.category_name, "Test Category")
        self.assertTrue(category.is_active)
        
        # 3. Update category
        category.category_name = "Updated Category"
        category.save()
        
        # 4. Verify update
        updated_category = Category.objects.get(id=category.id)
        self.assertEqual(updated_category.category_name, "Updated Category")
        
        # 5. Deactivate category
        category.is_active = False
        category.save()
        
        # 6. Verify deactivation
        deactivated_category = Category.objects.get(id=category.id)
        self.assertFalse(deactivated_category.is_active)
        
        # 7. Delete category
        category.delete()
        
        # 8. Verify deletion
        self.assertFalse(Category.objects.filter(id=category.id).exists())

    def test_category_organisation_relationship(self):
        """Test category-organisation relationship"""
        # Create multiple organisations
        org1 = Organisation.objects.create(
            name="Org 1",
            display_name="Organisation 1"
        )
        org2 = Organisation.objects.create(
            name="Org 2", 
            display_name="Organisation 2"
        )
        
        # Create categories for different organisations
        cat1 = Category.objects.create(
            category_name="Category 1",
            organisation=org1
        )
        cat2 = Category.objects.create(
            category_name="Category 2",
            organisation=org2
        )
        
        # Test relationship
        self.assertEqual(cat1.organisation, org1)
        self.assertEqual(cat2.organisation, org2)
        
        # Test reverse relationship
        self.assertIn(cat1, org1.categories.all())
        self.assertIn(cat2, org2.categories.all())

    def test_category_name_uniqueness(self):
        """Test category name uniqueness globally"""
        # Create category
        Category.objects.create(
            category_name="Unique Category Test",
            organisation=self.organisation
        )
        
        # Try to create another category with same name (should fail globally)
        with self.assertRaises(Exception):
            Category.objects.create(
                category_name="Unique Category Test",
                organisation=self.organisation
            )


class CategoryPerformanceTest(TestCase):
    """Performance tests for Category operations"""

    def setUp(self):
        """Set up test data"""
        self.organisation = Organisation.objects.create(
            name="Test Organisation",
            display_name="Test Organisation Display"
        )

    def test_bulk_category_creation(self):
        """Test creating multiple categories efficiently"""
        categories_data = [
            {
                'category_name': f'Category {i}',
                'category_description': f'Description for category {i}',
                'is_active': True,
                'organisation': self.organisation
            }
            for i in range(100)
        ]
        
        # Create categories
        categories = []
        for data in categories_data:
            category = Category.objects.create(**data)
            categories.append(category)
        
        # Verify all categories were created
        self.assertEqual(Category.objects.count(), 100)
        
        # Test bulk operations
        Category.objects.filter(is_active=True).update(is_active=False)
        self.assertEqual(Category.objects.filter(is_active=False).count(), 100)

    def test_category_queries(self):
        """Test efficient category queries"""
        # Create test data
        for i in range(50):
            Category.objects.create(
                category_name=f'Category {i}',
                is_active=i % 2 == 0,  # Alternate active/inactive
                organisation=self.organisation
            )
        
        # Test filtering queries
        active_categories = Category.objects.filter(is_active=True)
        inactive_categories = Category.objects.filter(is_active=False)
        
        self.assertEqual(active_categories.count(), 25)
        self.assertEqual(inactive_categories.count(), 25)
        
        # Test ordering
        ordered_categories = Category.objects.order_by('category_name')
        self.assertEqual(ordered_categories.first().category_name, 'Category 0')
        
        # Test select_related for organisation
        categories_with_org = Category.objects.select_related('organisation').all()
        for category in categories_with_org:
            # This should not trigger additional queries
            self.assertIsNotNone(category.organisation.name)
