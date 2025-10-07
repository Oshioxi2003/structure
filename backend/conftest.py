"""
Pytest configuration
"""
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    """Setup database for testing"""
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
