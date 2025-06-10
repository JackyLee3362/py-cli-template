import pytest

from {{cookiecutter.project_slug}}.base import Scaffold


@pytest.fixture(scope="session")
def scaffold():
    return Scaffold()
