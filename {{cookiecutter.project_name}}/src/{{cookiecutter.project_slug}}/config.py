from dynaconf import Dynaconf

from {{cookiecutter.project_slug}}.base.constant import CONFIG_DIR, CWD_PATH
from {{cookiecutter.project_slug}}.helper.merge import deepmerge


# Init Settings
def get_default_settings():
    settings = Dynaconf(
        root_path=CONFIG_DIR,
        environments=True,
        default_env="default",
        settings_files=["settings.*"],
        load_dotenv=True,
        dotenv_path=CWD_PATH,
    )
    return settings


# Update Settings
def update_settings(s, *, env: str = None, config_path: str = None, d: dict = None):
    env = env or s.env_for_dynaconf
    res = s.from_env(env)
    if config_path:
        res.load_file(path=config_path)
    if d:
        res_dict = res.to_dict()
        _upcase_d = {}
        for k, v in d.items():
            _upcase_d[k.upper()] = v
        _d = deepmerge(res_dict, _upcase_d)
        res.update(_d)
    return res
