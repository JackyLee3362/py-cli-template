import pytest

from {{cookiecutter.project_slug}}.base import Scaffold


@pytest.fixture(scope="session")
def scaffold():
    env = "testing"
    s = Scaffold()
    s.init_scaffold(force_env=env)
    assert s.settings.env_for_dynaconf == env
    return s