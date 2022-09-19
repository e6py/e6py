from pathlib import Path

from tests.setup import client


def test_get_single_pool():
    pool = client.get_pool(pool_id=1)
    assert pool.id == 1
    assert len(pool.posts) == pool.post_count == len(pool.post_ids)


def test_get_multiple_pools():
    pools = client.get_pools(id=[1, 2, 3])
    assert len(pools) == 3


def test_download_pool():
    p = Path("1")
    if p.exists():
        for file in p.glob("*"):
            file.unlink()
        p.rmdir()
    p.mkdir()
    pool = client.get_pool(pool_id=1)
    assert pool.download() == pool.post_count
    assert pool.download(path=str(p)) == 0
    for file in p.glob("*"):
        file.unlink()
    p.rmdir()
