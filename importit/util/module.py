from importlib.util import spec_from_loader, module_from_spec

from types import ModuleType


def create_empty_module(module_name: str, origin: str = None) -> ModuleType:
    """Creates a blank module.

    Args:
        module_name: The name to be given to the module.
        origin: The origin of the module. Defaults to None.

    Returns:
        A blank module.
    """
    spec = spec_from_loader(module_name, loader=None, origin=origin)
    module = module_from_spec(spec)
    return module


def create_module_from_code(
    module_name: str, source_code: str, origin: str = None
) -> ModuleType:
    """Creates a module from python code.

    Args:
        module_name: The name to be given to the module.
        source_code: The source code for the module.
        origin: The origin of the module. Defaults to None.

    Returns:
        A new module from the source code.
    """
    module = create_empty_module(module_name, origin)
    exec(source_code, module.__dict__)
    return module
