from logging.config import dictConfig

from dynaconf import Dynaconf

from {{cookiecutter.project_slug}}.base.cache import JsonCache
from {{cookiecutter.project_slug}}.base.constant import CACHE_DIR, CONFIG_DIR, CWD_PATH

# __all__ = ["config", "base_db", "Base", "AppDbClient", "DbClientBase"]


class Scaffold:
    debug: bool = False

    def __init__(self):
        # 初始化
        self.settings = None
        self.cache = None

    def init_scaffold(self, **kwargs):
        self.config_settings(CONFIG_DIR, CWD_PATH, **kwargs)
        self.config_logger(self.settings.logging.to_dict())
        self.config_cache(self.settings.app.cache.url)

    def config_settings(self, config_path, dotenv_path, **kwargs):
        # 初始配置
        self.settings = Dynaconf(
            root_path=config_path,
            environments=True,
            default_env="default",
            # 加载文件，分别为 preload -> settings_files -> includes
            preload=["preload.*"],
            settings_files=["logging.*", "settings.*"],
            includes=["include.*"],
            # merge_enabled=True, # 列表 merge 需要注意，可能会出现问题
            load_dotenv=True,
            dotenv_path=dotenv_path,
            **kwargs
        )

    def config_logger(self, d: dict):
        # 日志配置
        dictConfig(d)

    def config_cache(self, file_name: str):
        # 数据库配置
        self.cache = JsonCache(path=CACHE_DIR.joinpath(file_name))
