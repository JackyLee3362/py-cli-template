import tempfile
from pathlib import Path
from pprint import pprint

from {{cookiecutter.project_slug}}.base.cache import JsonCache


def test_config():
    dir_name = Path(tempfile.mkdtemp())
    cache = JsonCache(path=dir_name.joinpath("test.json"))
    cache.set("foo", 1)
    assert cache.get("foo") == 1
    cache.set("bar", 2)
    assert cache.get("bar") == 2
    cache.set("bar", None)
    assert cache.get("bar") is None

    pprint(cache.get("created-time"))
