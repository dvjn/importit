"""Defines various importer functions."""

import sys
from json import loads

from .util.file import get_local_file_content, get_remote_file_content
from .util.module import create_empty_module, create_module_from_code


def import_code(module_name, source_code, origin=None):
    """Imports python code as a module.

    Args:
        module_name: The name to be given to imported module.
        source_code: The code to be imported.
        origin: The origin of the code. Defaults to None.

    Returns:
        Python code imported as a module.

    Raises:
        ValueError: When invalid module name is passed.
    """
    if not module_name.isidentifier():
        raise ValueError("Invalid module name.")

    module = create_module_from_code(module_name, source_code, origin)
    sys.modules[module_name] = module

    return module


def import_local_file(module_name, file_path):
    """Imports a local file as a module.

    Args:
        module_name: The name to be given to the module.
        file_path: The path of the file to be imported.

    Returns:
        File from the path imported as a module.

    Raises:
        ValueError: When invalid module name is passed.
    """
    if not module_name.isidentifier():
        raise ValueError("Invalid module name.")

    source_code = get_local_file_content(file_path)

    module = create_module_from_code(module_name, source_code, origin=file_path)
    sys.modules[module_name] = module

    return module


def import_remote_file(module_name, url):
    """Imports a remote file as a module.

    Args:
        module_name: The name to be given to imported module.
        url: The url of file to be imported.

    Returns:
        File from the URL imported as a module.

    Raises:
        ValueError: When invalid module name is passed.
    """
    if not module_name.isidentifier():
        raise ValueError("Invalid module name.")

    source_code = get_remote_file_content(url)

    module = create_module_from_code(module_name, source_code, origin=url)
    sys.modules[module_name] = module

    return module


def import_gist(module_name, gist_id):
    """Imports a gist as a module.

    Args:
        module_name: The name to be given to imported module.
        gist_id: The id of the gist to be imported.

    Returns:
        Gist imported as a module.

    Raises:
        ValueError: When invalid module name is passed.
    """
    if not module_name.isidentifier():
        raise ValueError("Invalid module name.")

    gist = loads(get_remote_file_content("https://api.github.com/gists/" + gist_id))

    module = create_empty_module(module_name)

    for gist_file in gist["files"].values():
        if not gist_file["filename"].endswith(".py"):
            continue

        submodule_origin = gist_file["raw_url"]
        submodule_name = gist_file["filename"][:-3]
        submodule_content = (
            gist_file["content"]
            if not gist_file["truncated"]
            else get_remote_file_content(submodule_origin)
        )

        module.__dict__[submodule_name] = create_module_from_code(
            submodule_name, submodule_content, submodule_origin
        )

    sys.modules[module_name] = module

    return module
