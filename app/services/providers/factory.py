import os
import pkgutil
import importlib
import inspect
from .base import ImageProvider

PROVIDER_MODULE_PATH = os.path.dirname(__file__)
PROVIDER_PACKAGE = __name__.rpartition('.')[0] + '.providers'

print(PROVIDER_MODULE_PATH)