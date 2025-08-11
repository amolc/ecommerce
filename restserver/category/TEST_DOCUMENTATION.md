# Category API Test Documentation

This document provides comprehensive information about the test suite for the Category API.

## Overview

The Category API test suite includes multiple test classes covering different aspects of the application:

- **Model Tests**: Test the Category model functionality
- **Serializer Tests**: Test data serialization and validation
- **API Tests**: Test all API endpoints and responses
- **Integration Tests**: Test complete workflows and relationships
- **Performance Tests**: Test scalability and efficiency

## Test Classes

### 1. CategoryModelTest

Tests the Category model functionality including:

- ✅ Category creation and validation
- ✅ String representation
- ✅ Meta configuration
- ✅ Unique constraints
- ✅ Default values
- ✅ Field validation

**Key Test Methods:**
- `test_category_creation()` - Verifies category creation
- `test_category_string_representation()` - Tests `__str__` method
- `test_category_unique_name()` - Tests unique constraint
- `test_category_default_values()` - Tests default field values

### 2. CategorySerializerTest

Tests the CategorySerializer functionality including:

- ✅ Data validation
- ✅ Serialization of model instances
- ✅ Deserialization of data
- ✅ Partial updates
- ✅ Error handling

**Key Test Methods:**
- `test_category_serializer_valid_data()` - Tests valid data serialization
- `test_category_serializer_invalid_data()` - Tests invalid data handling
- `test_category_serializer_serialization()` - Tests model serialization
- `test_category_serializer_update()` - Tests partial updates

### 3. CategoryAPITest

Tests all API endpoints including:

- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ Authentication and authorization
- ✅ Error handling
- ✅ Filtering and pagination
- ✅ Custom actions (toggle status, active categories)

**Key Test Methods:**
- `test_list_categories()` - Tests GET /categories/
- `test_create_category()` - Tests POST /categories/
- `test_retrieve_category()` - Tests GET /categories/{id}/
- `test_update_category_full()` - Tests PUT /categories/{id}/
- `test_update_category_partial()` - Tests PATCH /categories/{id}/
- `test_delete_category()` - Tests DELETE /categories/{id}/
- `test_list_active_categories()` - Tests GET /categories/active/
- `test_toggle_category_status()` - Tests POST /categories/{id}/toggle_status/
- `test_unauthorized_access()` - Tests authentication requirements

### 4. CategoryIntegrationTest

Tests complete workflows and relationships:

- ✅ End-to-end category lifecycle
- ✅ Organisation relationships
- ✅ Data integrity
- ✅ Business logic validation

**Key Test Methods:**
- `test_category_workflow()` - Tests complete CRUD workflow
- `test_category_organisation_relationship()` - Tests foreign key relationships
- `test_category_name_uniqueness()` - Tests business rules

### 5. CategoryPerformanceTest

Tests performance and scalability:

- ✅ Bulk operations
- ✅ Query optimization
- ✅ Database efficiency
- ✅ Memory usage

**Key Test Methods:**
- `test_bulk_category_creation()` - Tests creating multiple categories
- `test_category_queries()` - Tests query efficiency

## Running Tests

### Method 1: Using Django's test command

```bash
# Run all category tests
python manage.py test category

# Run specific test class
python manage.py test category.tests.CategoryModelTest

# Run specific test method
python manage.py test category.tests.CategoryModelTest.test_category_creation

# Run with verbose output
python manage.py test category -v 2

# Run with coverage
coverage run --source='.' manage.py test category
coverage report
```

### Method 2: Using the test runner script

```bash
# Make the script executable
chmod +x category/run_tests.py

# Run tests
python category/run_tests.py
```

### Method 3: Using pytest (if installed)

```bash
# Install pytest-django
pip install pytest-django

# Run tests
pytest category/tests.py -v
```

## Test Data

### Test Data Factory

The `CategoryTestDataFactory` class provides utilities for creating test data:

```python
from category.test_config import CategoryTestDataFactory

# Create test user with token
user, token = CategoryTestDataFactory.create_test_user()

# Create test organisation
organisation = CategoryTestDataFactory.create_test_organisation()

# Create test category
category = CategoryTestDataFactory.create_test_category(organisation)

# Create multiple categories
categories = CategoryTestDataFactory.create_multiple_categories(organisation, count=10)
```

### Test Utilities

The `CategoryTestUtils` class provides helper functions:

```python
from category.test_config import CategoryTestUtils

# Get valid category data
valid_data = CategoryTestUtils.get_valid_category_data(organisation.id)

# Get invalid category data
invalid_data = CategoryTestUtils.get_invalid_category_data(organisation.id)

# Assert response structure
CategoryTestUtils.assert_category_response_structure(response.data)
```

## Test Configuration

### Environment Setup

Tests use the local settings by default. Ensure your test environment is properly configured:

```python
# settings/local.py or test settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ':memory:',  # Use in-memory database for tests
    }
}

# Disable logging during tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}
```

### Authentication

Tests use Django REST Framework's token authentication:

```python
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Create authenticated client
user = User.objects.create_user(username='testuser', password='testpass')
token = Token.objects.create(user=user)
client = APIClient()
client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
```

## Test Coverage

The test suite aims to achieve comprehensive coverage:

### Model Coverage (100%)
- ✅ Field definitions and constraints
- ✅ Meta configuration
- ✅ Methods and properties
- ✅ Validation logic

### Serializer Coverage (100%)
- ✅ Data validation
- ✅ Serialization/deserialization
- ✅ Error handling
- ✅ Partial updates

### API Coverage (100%)
- ✅ All CRUD endpoints
- ✅ Authentication requirements
- ✅ Error responses
- ✅ Custom actions
- ✅ Filtering and pagination

### Integration Coverage (100%)
- ✅ Complete workflows
- ✅ Relationship integrity
- ✅ Business logic validation

### Performance Coverage (90%)
- ✅ Bulk operations
- ✅ Query optimization
- ✅ Memory efficiency

## Best Practices

### Test Organization

1. **Arrange-Act-Assert Pattern**: Structure tests with clear setup, action, and verification
2. **Descriptive Names**: Use clear, descriptive test method names
3. **Single Responsibility**: Each test should verify one specific behavior
4. **Independent Tests**: Tests should not depend on each other

### Test Data Management

1. **Use Factories**: Create test data using factory classes
2. **Clean Up**: Use `setUp()` and `tearDown()` methods appropriately
3. **Realistic Data**: Use realistic test data that mirrors production scenarios
4. **Isolation**: Each test should create its own data

### Assertions

1. **Specific Assertions**: Use specific assertions rather than generic ones
2. **Meaningful Messages**: Provide clear error messages in assertions
3. **Multiple Assertions**: Test multiple aspects when appropriate
4. **Edge Cases**: Include tests for edge cases and error conditions

## Continuous Integration

### GitHub Actions Example

```yaml
name: Category Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python manage.py test category --verbosity=2
    
    - name: Generate coverage report
      run: |
        coverage run --source='.' manage.py test category
        coverage report
        coverage xml
```

## Troubleshooting

### Common Issues

1. **Database Errors**: Ensure test database is properly configured
2. **Import Errors**: Check that all required apps are in INSTALLED_APPS
3. **Authentication Errors**: Verify token creation and usage
4. **URL Errors**: Ensure URL patterns are correctly configured

### Debug Tips

1. **Use `-v 2` flag**: For verbose test output
2. **Use `--keepdb` flag**: To preserve test database between runs
3. **Use `--debug-mode`**: For detailed error information
4. **Check logs**: Review Django logs for additional error details

## Performance Benchmarks

### Expected Performance

- **Category Creation**: < 10ms per category
- **Category Retrieval**: < 5ms per category
- **Bulk Operations**: < 100ms for 100 categories
- **Query Optimization**: < 3 database queries for list operations

### Monitoring

Use Django Debug Toolbar or custom middleware to monitor:
- Database query count
- Response times
- Memory usage
- Cache hit rates

## Future Enhancements

### Planned Test Improvements

1. **Property-Based Testing**: Using Hypothesis for property-based tests
2. **Contract Testing**: API contract validation
3. **Load Testing**: Performance under high load
4. **Security Testing**: Penetration testing for API endpoints
5. **Mutation Testing**: Code mutation testing for better coverage

### Test Automation

1. **Auto-Generated Tests**: Generate tests from API specifications
2. **Visual Regression Testing**: For UI components
3. **API Contract Testing**: Validate API contracts
4. **Performance Regression Testing**: Automated performance monitoring
