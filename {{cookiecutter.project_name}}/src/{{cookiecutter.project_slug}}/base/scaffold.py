# __all__ = ["config", "base_db", "Base", "AppDbClient", "DbClientBase"]


from logging.config import dictConfig


class Scaffold:

    def __init__(self):
        # 初始化
        self.settings = None
        self.cache = None

    def init_scaffold(self, settings):
        self.settings = settings
        d = self.settings.logging.to_dict()
        dictConfig(d)

    @property
    def debug(self) -> bool:
        # 默认值 False
        return self.settings.app.debug

    @property
    def env(self) -> str:
        # 默认值 "development"
        return self.settings.env_for_dynaconf
