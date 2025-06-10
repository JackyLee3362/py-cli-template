import logging

import pytest

import {{cookiecutter.project_slug}}
from {{cookiecutter.project_slug}}.base import Scaffold
from {{cookiecutter.project_slug}}.base.constant import CONFIG_DIR, CWD_PATH


@pytest.fixture()
def scaffold_module():
    return Scaffold()


def test_scaffold_settings(scaffold_module: Scaffold):
    scaffold_module.config_settings(CONFIG_DIR, CWD_PATH)
    assert scaffold_module.settings is not None


def test_scaffold_logging(scaffold_module: Scaffold):
    scaffold_module.config_settings(CONFIG_DIR, CWD_PATH)
    s = scaffold_module.settings
    scaffold_module.config_logger(s.logging.to_dict())
    log = logging.getLogger({{cookiecutter.project_slug}}.__name__)
    assert len(log.handlers) > 0


def test_scaffold_cache(scaffold_module: Scaffold):
    scaffold_module.config_settings(CONFIG_DIR, CWD_PATH)
    s = scaffold_module.settings
    scaffold_module.config_cache(s.app.cache.url)
    assert scaffold_module.cache is not None


def test_scaffold_init(scaffold_module: Scaffold):
    scaffold_module.init_scaffold()
