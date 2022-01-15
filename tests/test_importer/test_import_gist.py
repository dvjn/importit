import pytest

from importit.importer import import_gist

GIST_API_URL = "https://api.github.com/gists/{}"
RAW_GIST_URL = "https://gist.githubusercontent.com/{}/{}/raw/{}/{}"

GOOD_SMALL_GIST_ID = "123abc456def789ghi012jkl345mno67"
GOOD_BIG_GIST_ID = "76onm543lkj210ihg987fed654cba321"
GOOD_BIG_FILE_ID = "321cba654fed987ihg210lkj543onm76"
BAD_GIST_ID = "not a gist id"

mock_gist_requests_map = {
    GIST_API_URL.format(GOOD_SMALL_GIST_ID): "tests/fixtures/good_small_gist_response.json",
    GIST_API_URL.format(GOOD_BIG_GIST_ID): "tests/fixtures/good_big_gist_response.json",
    RAW_GIST_URL.format("johndoe", GOOD_BIG_GIST_ID, GOOD_BIG_FILE_ID, "foo.py"): "tests/fixtures/foo.py",
}


def mock_get_remote_file_content(filepath):
    with open(mock_gist_requests_map[filepath], "r") as test_file:
        return test_file.read()


@pytest.fixture
def good_small_gist(monkeypatch):
    monkeypatch.setattr("importit.importer.get_remote_file_content", mock_get_remote_file_content)
    return GOOD_SMALL_GIST_ID


@pytest.fixture
def good_big_gist(monkeypatch):
    monkeypatch.setattr("importit.importer.get_remote_file_content", mock_get_remote_file_content)
    return GOOD_BIG_GIST_ID


@pytest.fixture
def bad_gist():
    return BAD_GIST_ID


def test_small_gist_import(good_small_gist):
    foo = import_gist("foo", good_small_gist)
    assert foo.__name__ == "foo"
    assert foo.foo.say_bar() == "bar"


def test_big_gist_import(good_big_gist):
    foo = import_gist("foo", good_big_gist)
    assert foo.__name__ == "foo"
    assert foo.bar.say_baz() == "baz"
    assert foo.baz.say_bar() == "bar"


def test_invalid_module_name(good_small_gist):
    with pytest.raises(ValueError):
        import_gist("foo bar", good_small_gist)


def test_invalid_file_import(bad_gist):
    with pytest.raises(Exception):
        import_gist("foo", bad_gist)
