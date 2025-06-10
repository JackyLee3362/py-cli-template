import logging
from os import PathLike
from typing import Union

from tinydb import Query, TinyDB

# 数据库连接
log = logging.getLogger(__name__)


class JsonCache:
    """json 数据库, 使用 json 文件存储，方便直接修改"""

    KEY_NAME = "key"
    VAL_NAME = "val"

    def __init__(self, path: PathLike):

        log.info(f"连接数据库: {path}")
        self._cache = TinyDB(path)
        self._query = Query()

    def set(self, key: str, val: Union[str, dict], tbl: str = None) -> None:
        """设置键值对

        Args:
            key (str): 键
            val (Union[str, dict]): 值
            tbl (str, optional): 表名, 默认为 None
        """
        _tbl = self._cache.table(tbl) if tbl else self._cache
        _key = self._query.__getattr__(self.KEY_NAME)
        _tbl.upsert({self.KEY_NAME: key, self.VAL_NAME: val}, _key == key)

    def get(self, key: str, tbl: str = None, default: Union[str, dict, list] = None):
        """获取键值对

        Args:
            key (str): 键
            default (Union[str, dict, list], optional): 默认值, 默认为 None.
            tbl (str, optional): 表名, 默认为 None.
        """
        _tbl = self._cache.table(tbl) if tbl else self._cache
        _key = self._query.__getattr__(self.KEY_NAME)
        _res = _tbl.get(_key == key)
        if _res:
            return _res.get(self.VAL_NAME)
        return default

    def get_all(self, tbl: str = None) -> dict:
        """在一个表中获取所有值
        Args:
            tbl (str, optional): 表名. 默认为 None.

        Returns:
            _type_: _description_
        """
        table = self._cache.table(tbl) if tbl else self._cache
        _res = {}
        for item in table.all():
            _key = item.get(self.KEY_NAME)
            _val = item.get(self.VAL_NAME)
            _res[_key] = _val
        return _res

    def close(self):
        log.info("关闭缓存")
        self._cache.close()
