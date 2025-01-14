from ._compat import to_str as to_str
from re import Match as Match
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Query
from sqlalchemy import Table
from typing import Any
from typing import ClassVar, TypeVar, Generic, Type
from . import BaseQuery

def should_set_tablename(cls: Any) -> bool: ...

camelcase_re: Any

def camel_to_snake_case(name: str) -> str: ...

class NameMetaMixin:
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...
    def __table_cls__(cls, *args: Any, **kwargs: Any) -> Any: ...

class BindMetaMixin:
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...

class DefaultMeta(NameMetaMixin, BindMetaMixin, DeclarativeMeta): ...

class Model:
    query_class: ClassVar[Type[BaseQuery[Model]]] = ...
    query: ClassVar[BaseQuery[Model]]
    __table__: ClassVar[Table]
