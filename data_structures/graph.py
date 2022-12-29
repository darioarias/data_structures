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

    def __iter__(self) -> typing.Iterator[typing.Union[_Vertex[_T], float]]:
        yield from (self.source, self.destination, self.weight)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(source={self.source}, "
            f"destination={self.destination}, weight={self.weight})"
        )

    def __str__(self) -> str:
        return f"{str(self.source)} -({self.weight})-> {str(self.destination)}"


class _Graphable(typing.Generic[_T]):
    def __init__(self, directed: bool = True) -> None:
        self.adjacency_list: dict[_Vertex[_T], list[_Edge[_T]]] = {}
        self._type = directed

    def create_vertex(self, data: _T) -> _Vertex[_T]:
        return _Vertex(data)

    def add(
        self,
        source: _Vertex[_T],
        destination: _Vertex[_T],
        weight: int | float = 0,
    ) -> None:
        ...

    def weight(self, source: _Vertex[_T], destination: _Vertex[_T]) -> int | float:
        ...

    def edges(self, source: _Vertex[_T]) -> list[_Edge[_T]]:
        ...


class AdjacencyList(_Graphable[_T]):
    def create_vertex(self, data: _T) -> _Vertex[_T]:
        vertex = _Vertex(data=data)

        if not (vertex in self.adjacency_list):
            self.adjacency_list[vertex] = []

        return vertex

    def add_directed_edge(
        self, source: _Vertex[_T], destination: _Vertex[_T], weight: int | float = 0
    ):
        edge = _Edge(source=source, destination=destination, weight=weight)
        self.adjacency_list.setdefault(source, []).append(edge)

    def add_undirected_edge(
        self, vertices: tuple[_Vertex[_T], _Vertex[_T]], weight: float | int = 0
    ):
        source, destination = vertices
        self.add_directed_edge(source=source, destination=destination, weight=weight)
        self.add_directed_edge(source=destination, destination=source, weight=weight)

    def add(
        self,
        source: _Vertex[_T],
        destination: _Vertex[_T],
        weight: float = 0,
    ) -> None:
        match self._type:
            case True:
                self.add_directed_edge(
                    source=source, destination=destination, weight=weight
                )
            case _:
                self.add_undirected_edge(vertices=(source, destination), weight=weight)

    def weight(
        self, source: _Vertex[_T], destination: _Vertex[_T]
    ) -> typing.Optional[int | float]:
        if not (source in self.adjacency_list):
            return None

        for edge in self.adjacency_list[source]:
            if edge.destination == destination:
                return edge.weight

        return None

    def edges(self, source: _Vertex[_T]) -> typing.Optional[list[_Edge[_T]]]:
        return self.adjacency_list.get(source, None)

    def __str__(self) -> str:
        msg = ["{\n"]
        space = "  " * 2
        inner_msg = []

        def edges_to_str(items: list[_Edge[_T]]) -> typing.Iterator[str]:
            return (f"{str(edge.destination)}, cost: {edge.weight}" for edge in items)

        for key in self.adjacency_list:
            new_line = f"\n{space * 2}  "
            inner_str = f"{new_line}".join(edges_to_str(self.adjacency_list[key]))
            inner_str += f"\n{space*2}]" if inner_str else "]"
            if inner_str != "]":
                inner_str = f"{new_line}{inner_str}"
            inner_msg.append(f"{space}{str(key)}: [{inner_str}")

        msg.append("\n".join(inner_msg))
        msg.append("\n}")
        return "".join(msg)
