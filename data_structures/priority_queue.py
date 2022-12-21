import operator
from typing import Callable, Generic, Iterable, Iterator, Optional, TypeVar, Union, cast

from ._protocols import CT
from .heap import Heap

_T = TypeVar("_T")


def _default_key(a: _T, b: _T) -> bool:
    try:
        return operator.lt(cast(CT, a), cast(CT, b))
    except:
        raise TypeError(f"Key function missing")


class PriorityQueue(Generic[_T]):
    pass


__all__ = ["PriorityQueue"]
