from datetime import datetime

from e6py.models import Category
from e6py.utils.converters import convert_timestamp


def test_convert_timestamp():
    now = datetime.now()
    assert convert_timestamp(now) == now
    assert convert_timestamp(now.isoformat()) == now


def test_category_enum():
    assert "General" in Category
    assert 0 in Category
