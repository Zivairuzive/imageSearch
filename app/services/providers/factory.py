import os
import pkgutil
import importlib
import inspect
from .base import ImageProvider
from typing import Dict
from functools import lru_cache



PROVIDER_MODULE_PATH = os.path.dirname(__file__)
PROVIDER_PACKAGE = __name__.rpartition('.')[0] + '.providers'
PROVIDER_SUFFIX_NAME = "_provider"
SKIP_LOAD = ['__init__', 'base', 'factory']

ProvidersReturnType = Dict[str, ImageProvider]



@lru_cache(maxsize=1)
def load_providers()-> ProvidersReturnType:
    providers:ProvidersReturnType = {}
    
    for _, module_name, is_pkg in pkgutil.iter_modules([PROVIDER_MODULE_PATH]):
        if is_pkg and module_name in SKIP_LOAD:
            continue
        module = importlib.import_module(f"{PROVIDER_PACKAGE}.{module_name}")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if(
                issubclass(obj, ImageProvider) and obj is not ImageProvider
            ):
                provider_name = module_name.replace(PROVIDER_SUFFIX_NAME, '')
                providers[provider_name] = obj()
    return providers