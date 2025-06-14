import logging
import sys
from pathlib import Path

from dotenv import load_dotenv

# 环境变量
sys.path.insert(0, str(Path(__file__).resolve().parent.joinpath("src")))
# 加载 .env 变量
load_dotenv()

if __name__ == "__main__":
    from {{cookiecutter.project_slug}}.cli import cli

    log = logging.getLogger(__name__)

    # 捕获全局异常
    try:
        cli()
    except Exception as e:
        log.error(e)
