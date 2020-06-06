from importit.importer import import_gist

import pytest


def mock_gist_content(url):
    return """{
    "files": {
        "hello.py": {
            "raw_url": "https://gist.githubusercontent.com/mock-gist/hello.py",
            "truncated": false,
            "content": "def say_hello():\\n    return \\"hello\\""
        },
        "hello_again.py": {
            "raw_url": "https://gist.githubusercontent.com/mock-gist/hello_again.py",
            "truncated": false,
            "content": "def say_hello_again():\\n    return \\"hello again\\""
        }
    }
}"""


@pytest.fixture
def test_gist_id(monkeypatch):
    monkeypatch.setattr("importit.importer.get_remote_file_content", mock_gist_content)
    return "mock-gist-id"


def test_import(test_gist_id):
    import_gist("hellos", test_gist_id)


def test_module_name(test_gist_id):
    hellos = import_gist("hellos", test_gist_id)
    assert hellos.__name__ == "hellos"


def test_submodule_names(test_gist_id):
    hellos = import_gist("hellos", test_gist_id)
    assert hellos.hello.__name__ == "hello"
    assert hellos.hello_again.__name__ == "hello_again"


def test_submodules(test_gist_id):
    hellos = import_gist("hellos", test_gist_id)
    assert hellos.hello.say_hello() == "hello"
    assert hellos.hello_again.say_hello_again() == "hello again"
