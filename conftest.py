"""Root conftest: configure Django settings before pytest-django loads."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'blogicum'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'blogicum.settings'
