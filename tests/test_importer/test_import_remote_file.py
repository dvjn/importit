import pytest

from importit.importer import import_remote_file

mock_remote_files_map = {
    "https://foo.bar/foo.py": "tests/fixtures/foo.py",
    "http://baz.foo/foo.txt": "tests/fixtures/foo.txt",
}


def mock_get_remote_file_content(filepath):
    with open(mock_remote_files_map[filepath], "r") as test_file:
        return test_file.read()


@pytest.fixture
def python_file(monkeypatch):
    monkeypatch.setattr("importit.importer.get_remote_file_content", mock_get_remote_file_content)
    return "https://foo.bar/foo.py"


@pytest.fixture
def bad_file(monkeypatch):
    monkeypatch.setattr("importit.importer.get_remote_file_content", mock_get_remote_file_content)
    return "http://baz.foo/foo.txt"


def test_normal_file_import(python_file):
    foo = import_remote_file("foo", python_file)
    assert foo.__name__ == "foo"
    assert foo.say_bar() == "bar"


def test_invalid_module_name(python_file):
    with pytest.raises(ValueError):
        import_remote_file("foo bar", python_file)


def test_invalid_file_import(bad_file):
    with pytest.raises(SyntaxError):
        import_remote_file("foo", bad_file)
