from importit.importer import import_code

import pytest


@pytest.fixture
def test_hello_code():
    return "def say_hello():\n    return 'hello'"


def test_import(test_hello_code):
    import_code("hello", test_hello_code)


def test_import_name(test_hello_code):
    hello = import_code("hello", test_hello_code)
    assert hello.__name__ == "hello"


def test_import_function(test_hello_code):
    hello = import_code("hello", test_hello_code)
    assert hello.say_hello() == "hello"
