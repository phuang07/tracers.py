from pathlib import PurePath
from typing import Any, Dict, List, Tuple, TypeVar, Union


PathLike = Union[str, bytes, PurePath]
Number = Union[int, float]

# Types which are serializable by the default JSONEncoder
# Recursive types aren't supported yet. See https://github.com/python/mypy/issues/731
_Keys = Union[str, int, float, bool, None]
_Collections = Union[Dict[_Keys, Any], List[Any], Tuple[Any]]
Serializable = Union[_Collections, _Keys]

_T = TypeVar("_T", _Collections, _Keys)
SerializableSequence = Union[List[_T], Tuple[_T]]


class Undefined:
    pass


UNDEFINED = Undefined()
