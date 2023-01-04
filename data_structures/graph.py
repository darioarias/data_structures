from __future__ import annotations

import enum
import operator
import typing
from collections import OrderedDict, defaultdict

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
    def __init__(
        self,
        directed: bool = True,
    ) -> None:
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

    def dijkstra(
        self, start: _Vertex[_T], end: _Vertex[_T]
    ) -> typing.Iterable[tuple[_Vertex[_T], float]]:
        ...

    def minimum_spanning_tree(self) -> AdjacencyList[_T]:
        ...

    def a_star(
        self,
        start: _Vertex[_T],
        end: _Vertex[_T],
        __heuristic: typing.Callable[[_T, _T], float] = lambda a, b: 0.0,
    ) -> typing.Iterable[tuple[_T, float]]:
        ...


class AdjacencyList(_Graphable[_T]):
    def __init__(
        self,
        __items: typing.Optional[typing.Union[list[_T], typing.Iterable[_T]]] = None,
        directed: bool = True,
    ) -> None:
        super().__init__(directed)
        self.adjacency_list: dict[_Vertex[_T], list[_Edge[_T]]] = OrderedDict()

        if __items is not None:
            for item in __items:
                self.create_vertex(item)

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

    def _visit_vertecies(
        self,
        visited: set[_Vertex[_T]],
        start: _Vertex[_T],
        end: _Vertex[_T],
        heuristic: typing.Callable[[_T, _T], float] = lambda a, b: 0.0,
    ) -> dict[_Vertex[_T], tuple[_Vertex[_T], float]]:
        queue: PriorityQueue[_Edge[_T]] = PriorityQueue(
            [_Edge(start, start, 0.0)],
            key=lambda a, b: operator.lt(
                a.weight + getattr(a, "estimate", 0.0),
                b.weight + getattr(b, "estimate", 0.0),
            ),
        )

        record: dict[_Vertex[_T], tuple[_Vertex[_T], float]] = defaultdict(
            lambda: (
                _Vertex(
                    data=type(
                        _T.__class__
                    )  # trying to create an default instance of the type being used.
                ),
                float("-inf"),
            )
        )

        while queue:
            src, dst, weight = queue.dequeue()
            visited.add(dst)

            if record[dst][1] == float("-inf") and dst != start:
                record[dst] = (src, weight)

            if dst == end:
                break

            for neighbor in self.adjacency_list[dst]:
                if neighbor not in visited:
                    e_src, e_dst, e_wgt = neighbor
                    edge = _Edge(e_src, e_dst, e_wgt + weight)
                    setattr(edge, "estimate", heuristic(e_dst._data, end._data))
                    queue.enqueue(edge)

        return record

    def _build_path(
        self,
        record: dict[_Vertex[_T], tuple[_Vertex[_T], float]],
        start: _Vertex[_T],
        end: _Vertex[_T],
    ) -> typing.Iterator[tuple[_T, float]]:
        path: list[tuple[_T, float]] = []

        while True:
            current, cost = record[end]
            if cost == float("-inf"):
                if len(path) == 0:
                    raise ValueError(f"No path exists between {start} and {end}")
                path.append((start._data, 0))
                return reversed(path)

            path.append((end._data, cost))
            end = current

    def dijkstra(
        self, start: _Vertex[_T], end: _Vertex[_T]
    ) -> typing.Iterator[tuple[_T, float]]:
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError(f"No path exists between {start} and {end}")

        record: dict[_Vertex[_T], tuple[_Vertex[_T], float]] = self._visit_vertecies(
            visited=set(), start=start, end=end
        )

        return self._build_path(record, start, end)

    def minimum_spanning_tree(self) -> AdjacencyList[_T]:
        if self._type:
            raise ValueError(
                "Cannot create Minimum Spanning Tree out of a directed graph"
            )

        start: typing.Optional[_Vertex[_T]] = None
        for key in self.adjacency_list:
            start = key
            break

        assert start is not None, "No Minimum Spanning Tree for empty graph"

        visited: set[_Vertex[_T]] = set([start])
        spanning_tree: AdjacencyList[_T] = AdjacencyList(directed=self._type)
        pQueue: PriorityQueue[_Edge[_T]] = PriorityQueue(
            [edge for edge in self.adjacency_list[start]],
            key=lambda a, b: operator.lt(a.weight, b.weight),
        )

        while pQueue:
            src, dst, weight = pQueue.dequeue()

            if dst in visited:
                continue
            visited.add(dst)

            spanning_tree.add(dst, src, weight)
            for edge in self.adjacency_list[dst]:
                pQueue.enqueue(edge)

        return spanning_tree

    def a_star(
        self,
        start: _Vertex[_T],
        end: _Vertex[_T],
        __heuristic: typing.Callable[[_T, _T], float] = lambda a, b: 0.0,
    ) -> typing.Iterable[tuple[_T, float]]:

        record: dict[_Vertex[_T], tuple[_Vertex[_T], float]] = self._visit_vertecies(
            visited=set(), start=start, end=end, heuristic=__heuristic
        )

        return self._build_path(record, start, end)

    def __iter__(self) -> typing.Iterator[_Vertex[_T]]:
        yield from self.adjacency_list.keys()

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
