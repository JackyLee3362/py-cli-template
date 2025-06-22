from dynaconf import Dynaconf

from {{cookiecutter.project_slug}}.base.scaffold import Scaffold


class App(Scaffold):

    def __init__(self):
        pass

    def init_app(self, settings: Dynaconf):
        self.init_scaffold(settings)
        if self.debug:
            print("Need to print some debug info...")
