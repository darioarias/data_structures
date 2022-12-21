import operator
from typing import Callable, Generic, Iterable, Iterator, Optional, TypeVar, Union, cast

from ._protocols import CT
from .heap import Heap

_T = TypeVar("_T")


class PriorityQueue(Generic[_T]):
    pass


__all__ = ["PriorityQueue"]
