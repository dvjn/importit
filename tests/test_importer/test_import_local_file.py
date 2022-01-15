import pytest
from importit.importer import import_local_file

mock_local_files_map = {
    "/home/johndoe/foo.py": "tests/fixtures/foo.py",
    "/home/johndoe/foo.txt": "tests/fixtures/foo.txt",
}


def mock_get_local_file_content(filepath):
    with open(mock_local_files_map[filepath], "r") as test_file:
        return test_file.read()


@pytest.fixture
def python_file(monkeypatch):
    monkeypatch.setattr("importit.importer.get_local_file_content", mock_get_local_file_content)
    return "/home/johndoe/foo.py"


@pytest.fixture
def bad_file(monkeypatch):
    monkeypatch.setattr("importit.importer.get_local_file_content", mock_get_local_file_content)
    return "/home/johndoe/foo.txt"


def test_normal_file_import(python_file):
    foo = import_local_file("foo", python_file)
    assert foo.__name__ == "foo"
    assert foo.say_bar() == "bar"


def test_invalid_module_name(python_file):
    with pytest.raises(ValueError):
        import_local_file("foo bar", python_file)


def test_invalid_file_import(bad_file):
    with pytest.raises(SyntaxError):
        import_local_file("foo", bad_file)
