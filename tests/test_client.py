import pytest

from e6py.client import E621Client as Client
from tests.setup import client


def test_client_init():
    with pytest.raises(ValueError):
        _ = Client(login="", api_key="")


def test_client_errors():
    assert client.get_post(4_000_000_000) is None
