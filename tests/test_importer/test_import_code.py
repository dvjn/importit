import pytest
from importit.importer import import_code


def test_normal_code_import():
    foo = import_code(
        "foo",
        "def say_bar():\n    return 'bar'",
    )
    assert foo.__name__ == "foo"
    assert foo.say_bar() == "bar"


def test_invalid_module_name():
    with pytest.raises(ValueError):
        import_code("foo bar", "")


def test_invalid_code_import():
    with pytest.raises(SyntaxError):
        import_code("foo", "this is not a piece of python code")
