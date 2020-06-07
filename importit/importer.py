"""Defines various importer functions."""

import sys
from json import loads
from .util.file import get_local_file_content, get_remote_file_content
from .util.module import create_empty_module, create_module_from_code

from types import ModuleType


def import_code(module_name: str, source_code: str, origin: str = None) -> ModuleType:
    """Imports python code as a module.

    Args:
        module_name: The name to be given to imported module.
        source_code: The code to be imported.
        origin: The origin of the code. Defaults to None.

    Returns:
        Python code imported as a module.

    Raises:
        ImportError: Raised when the code can't be imported.
    """
    module = create_module_from_code(module_name, source_code, origin)
    sys.modules[module_name] = module

    return module


def import_local_file(module_name: str, file_path: str) -> ModuleType:
    """Imports a local file as a module.

    Args:
        module_name: The name to be given to the module.
        file_path: The path of the file to be imported.

    Returns:
        File from the path imported as a module.

    Raises:
        ImportError: Raised when the file can't be imported.
    """
    source_code = get_local_file_content(file_path)

    module = create_module_from_code(module_name, source_code, origin=file_path)
    sys.modules[module_name] = module

    return module


def import_remote_file(module_name: str, url: str) -> ModuleType:
    """Imports a remote file as a module.

    Args:
        module_name: The name to be given to imported module.
        url: The url of file to be imported.

    Returns:
        File from the URL imported as a module.

    Raises:
        ImportError: Raised when the file can't be imported.
    """
    source_code = get_remote_file_content(url)

    module = create_module_from_code(module_name, source_code, origin=url)
    sys.modules[module_name] = module

    return module


def import_gist(module_name: str, gist_id: str) -> ModuleType:
    """Imports a gist as a module.

    Args:
        module_name: The name to be given to imported module.
        gist_id: The id of the gist to be imported.

    Returns:
        Gist imported as a module.

    Raises:
        ImportError: Raised when the gist can't be imported.
    """
    gist = loads(get_remote_file_content("https://api.github.com/gists/" + gist_id))

    module = create_empty_module(module_name)

    submodules = {
        filename[:-3]: create_module_from_code(
            filename[:-3], gist_file["content"], gist_file["raw_url"]
        )
        for filename, gist_file in gist["files"].items()
        if filename.endswith(".py")
    }

    module.__dict__.update(submodules)
    sys.modules[module_name] = module

    return module
