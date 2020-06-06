from importit.importer import import_remote_file

import pytest


def mock_remote_file_content(url):
    return "def say_hello():\n    return 'hello'"


@pytest.fixture
def mock_hello_file(monkeypatch):
    monkeypatch.setattr(
        "importit.importer.get_remote_file_content", mock_remote_file_content
    )
    return "https://mock_url.com/hello.py"


def test_import(mock_hello_file):
    import_remote_file("hello", mock_hello_file)


def test_import_name(mock_hello_file):
    hello = import_remote_file("hello", mock_hello_file)
    assert hello.__name__ == "hello"


def test_import_function(mock_hello_file):
    hello = import_remote_file("hello", mock_hello_file)
    assert hello.say_hello() == "hello"
