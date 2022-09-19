from pathlib import Path

import pytest
from e6py.models.post import File, ensure_cls
from tests.setup import client


def test_get_single_post():
    post = client.get_post(1)
    assert post.id == 1
    assert post.to_dict().get("id") == 1


def test_get_multiple_posts():
    posts = client.get_posts(after=1, limit=5)
    assert len(posts) == 5


def test_wrong_ext():
    with pytest.raises(ValueError):
        _ = File(width=120, height=120, ext="bad_ext", size=120, md5="bad_md5")


def test_ensure_cls():
    f = File(width=120, height=120, ext="jpg", size=120, md5="bad_md5")
    converter = ensure_cls(File)
    f2 = converter(f)
    assert f2 == f

    converter_list = ensure_cls(File, lst=True)
    f_list = [f, f2]
    f_list2 = converter_list(f_list)
    assert f_list == f_list2

    f_dict = {"width": 120, "height": 120, "ext": "jpg", "size": 120, "md5": "bad_md5"}
    f3 = converter(f_dict)
    assert f3 == f

    assert f3.to_dict() == f_dict

    f_dict_list = [f_dict, f_dict]
    f_list3 = converter_list(f_dict_list)
    assert f_list3 == f_list


def test_download():
    post = client.get_post(5)
    file = Path(f"{post.file.md5}.{post.file.ext}")
    if file.exists():
        file.unlink()
    assert post.download() == True
    assert post.download() == False
    post._downloaded = False
    assert post.download() == False
    file.unlink()
