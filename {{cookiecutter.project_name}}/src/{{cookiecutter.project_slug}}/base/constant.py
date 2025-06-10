# 参考 PyInstaller
import os
from pathlib import Path

__version__ = "0.0.1"

PACKAGE_PATH = Path(__file__).parent

SRC_PATH = Path(__file__).parent.parent

CWD_PATH = Path(os.getcwd())
LOG_DIR = Path(os.getcwd(), "logs")
CONFIG_DIR = Path(os.getcwd(), "config")
DB_DIR = Path(os.getcwd(), "db")
CACHE_DIR = Path(os.getcwd(), "cache")


def init_dir():
    """初始化创建目录"""
    LOG_DIR.mkdir(exist_ok=True, parents=True)
    CONFIG_DIR.mkdir(exist_ok=True, parents=True)
    DB_DIR.mkdir(exist_ok=True, parents=True)
    CACHE_DIR.mkdir(exist_ok=True, parents=True)
