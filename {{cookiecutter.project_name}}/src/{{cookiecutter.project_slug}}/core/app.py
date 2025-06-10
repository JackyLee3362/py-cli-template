import logging

from {{cookiecutter.project_slug}}.base.scaffold import Scaffold

log = logging.getLogger(__name__)


class App(Scaffold):

    def init_app(self):...

