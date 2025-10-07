"""
Settings package - Import settings based on environment
"""
import os

env = os.environ.get('DJANGO_ENV', 'dev')

if env == 'prod' or env == 'production':
    from .prod import *
else:
    from .dev import *
