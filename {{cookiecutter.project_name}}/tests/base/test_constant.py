from {{cookiecutter.project_slug}}.base.constant import (
    CACHE_DIR,
    CONFIG_DIR,
    DB_DIR,
    LOG_DIR,
    init_dir,
)


def test_config():
    init_dir()
    assert LOG_DIR.exists()
    assert CACHE_DIR.exists()
    assert DB_DIR.exists()
    assert CONFIG_DIR.exists()
