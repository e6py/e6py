from e6py.models.tag import convert_tags
from tests.setup import client


def test_get_single_tag():
    tag = client.get_tag(1)
    assert tag.id == 1


def test_get_multiple_tags():
    tags = client.get_tags(name_matches="dragon*")
    assert len(tags) > 0


def test_convert_tags():
    tags = convert_tags("a b c")
    assert tags == ["a", "b", "c"]
