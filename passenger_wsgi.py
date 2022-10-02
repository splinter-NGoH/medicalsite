import os
import sys
from medicalrcommerce.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicalrcommerce.settings")