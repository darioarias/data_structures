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

    def __repr__(self) -> str:
        return f"{type(self).__name__}(data={self._data!r})"

    def __str__(self) -> str:
        return f"{str(self._data)}"


class _Edge(tuple["_Vertex[_T]", "_Vertex[_T]", float]):
    def __new__(
        cls, source: _Vertex[_T], destination: _Vertex[_T], weight: float = 0
    ) -> _Edge[_T]:
        return tuple.__new__(cls, (source, destination, weight))

    def __init__(
        self, source: _Vertex[_T], destination: _Vertex[_T], weight: float = 0
    ) -> None:
        self.source: _Vertex[_T] = source
        self.destination: _Vertex[_T] = destination
        self.weight: float = weight

    def __hash__(self) -> int:
        return hash((self.source, self.destination, self.weight))

    def __eq__(self, rhs: _Edge[_T]) -> bool:
        try:
            return (
                self.destination == rhs.destination
                and self.destination == rhs.destination
                and self.weight == rhs.weight
            )
        except:
            return NotImplemented
