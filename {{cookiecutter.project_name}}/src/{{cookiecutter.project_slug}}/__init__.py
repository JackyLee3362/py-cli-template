# 参考 PyInstaller
import os

__version__ = "0.0.1"

PACKAGE_PATH = os.path.abspath(os.path.dirname(__file__))
SRC_PATH = os.path.dirname(PACKAGE_PATH)

DEFAULT_CWD_PATH = os.getcwd()
DEFAULT_LOG_PATH = os.path.join(os.getcwd(), "logs")
DEFAULT_CONFIG_PATH = os.path.join(os.getcwd(), "config")
DEFAULT_DB_PATH = os.path.join(os.getcwd(), "db")
