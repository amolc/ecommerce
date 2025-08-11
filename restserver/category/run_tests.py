#!/usr/bin/env python
"""
Test runner script for Category tests
"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

def run_tests():
    """Run the Category tests"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restserver.settings.local')
    django.setup()
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # Run specific test classes
    test_classes = [
        'category.tests.CategoryModelTest',
        'category.tests.CategorySerializerTest', 
        'category.tests.CategoryAPITest',
        'category.tests.CategoryIntegrationTest',
        'category.tests.CategoryPerformanceTest'
    ]
    
    failures = test_runner.run_tests(test_classes)
    return failures

if __name__ == '__main__':
    failures = run_tests()
    if failures:
        sys.exit(1)
