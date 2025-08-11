"""
Test configuration and utilities for Category tests
"""
from customers.models import Customer
from rest_framework.authtoken.models import Token
from organisations.models import Organisation
from .models import Category


class CategoryTestDataFactory:
    """Factory class for creating test data"""
    
    @staticmethod
    def create_test_user(mobile_number='1234567890', email='test@example.com', password='testpass123', organisation=None):
        """Create a test user with token"""
        if organisation is None:
            organisation = CategoryTestDataFactory.create_test_organisation()
        
        user = Customer.objects.create_user(
            mobile_number=mobile_number,
            email=email,
            password=password,
            first_name='Test',
            last_name='User',
            organisation=organisation
        )
        token = Token.objects.create(user=user)
        return user, token
    
    @staticmethod
    def create_test_organisation(name="Test Organisation", display_name="Test Organisation Display"):
        """Create a test organisation"""
        return Organisation.objects.create(
            name=name,
            display_name=display_name
        )
    
    @staticmethod
    def create_test_category(organisation, **kwargs):
        """Create a test category with default values"""
        defaults = {
            'category_name': 'Test Category',
            'category_description': 'Test category description',
            'is_active': True,
            'organisation': organisation
        }
        defaults.update(kwargs)
        return Category.objects.create(**defaults)
    
    @staticmethod
    def create_multiple_categories(organisation, count=5, prefix="Category"):
        """Create multiple test categories"""
        categories = []
        for i in range(count):
            category = Category.objects.create(
                category_name=f"{prefix} {i}",
                category_description=f"Description for {prefix} {i}",
                is_active=i % 2 == 0,  # Alternate active/inactive
                organisation=organisation
            )
            categories.append(category)
        return categories


class CategoryTestUtils:
    """Utility functions for Category tests"""
    
    @staticmethod
    def get_valid_category_data(organisation_id, **kwargs):
        """Get valid category data for testing"""
        defaults = {
            'category_name': 'Test Category',
            'category_description': 'Test category description',
            'is_active': True,
            'organisation': organisation_id
        }
        defaults.update(kwargs)
        return defaults
    
    @staticmethod
    def get_invalid_category_data(organisation_id, **kwargs):
        """Get invalid category data for testing"""
        defaults = {
            'category_name': '',  # Empty name
            'category_description': 'Test description',
            'is_active': True,
            'organisation': organisation_id
        }
        defaults.update(kwargs)
        return defaults
    
    @staticmethod
    def assert_category_response_structure(response_data):
        """Assert that category response has correct structure"""
        required_fields = ['status', 'message', 'data']
        for field in required_fields:
            assert field in response_data, f"Response missing required field: {field}"
        
        if response_data['status'] == 'success':
            assert 'data' in response_data, "Success response must have data field"
    
    @staticmethod
    def assert_category_data_structure(category_data):
        """Assert that category data has correct structure"""
        required_fields = [
            'id', 'category_name', 'category_description', 'is_active',
            'created_at', 'updated_at', 'organisation'
        ]
        for field in required_fields:
            assert field in category_data, f"Category data missing required field: {field}"


# Test constants
TEST_CATEGORY_NAMES = [
    "Electronics",
    "Clothing",
    "Books",
    "Home & Garden",
    "Sports & Outdoors",
    "Automotive",
    "Health & Beauty",
    "Toys & Games",
    "Food & Beverages",
    "Jewelry & Watches"
]

TEST_CATEGORY_DESCRIPTIONS = [
    "Electronic devices and accessories",
    "Clothing, shoes, and fashion accessories",
    "Books, magazines, and educational materials",
    "Home improvement and garden supplies",
    "Sports equipment and outdoor gear",
    "Automotive parts and accessories",
    "Health and beauty products",
    "Toys, games, and entertainment",
    "Food, beverages, and kitchen supplies",
    "Jewelry, watches, and luxury items"
]
