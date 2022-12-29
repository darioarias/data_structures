from __future__ import annotations

import enum
import operator
import typing
from collections import defaultdict

from .priority_queue import PriorityQueue

_T = typing.TypeVar("_T")


class _Vertex(typing.Generic[_T]):
    def __init__(self, data: _T) -> None:
        self._data = data

    def __iter__(self) -> typing.Iterator[_T]:
        yield self._data

    def __eq__(self, __o: _Vertex[_T]) -> bool:
        try:
            return self._data == __o._data
        except:
            return NotImplemented

    def __hash__(self) -> int:
        return hash(self._data)
