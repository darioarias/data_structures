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
    def __init__(
        self,
        __items: Optional[Union[list[_T], Iterable[_T]]] = None,
        key: Callable[[_T, _T], bool] = _default_key,
    ) -> None:
        _items: list[_T] = []
        if isinstance(__items, list):
            _items = __items
        elif isinstance(__items, Iterable):
            _items = [item for item in __items]

        heap: Heap[_T] = Heap()  # type: ignore
        heap._sort = key
        heap._heapify(_items)

        self.heap = heap

    def enqueue(self, value: _T) -> None:
        """Inserts an element into the queue."""
        self.heap.insert(value)

    def dequeue(self) -> Optional[_T]:
        """Removes the element with the highest priority and returns it. Returns `None` if the queue is empty."""
        return self.heap.remove()

    @property
    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.heap.size == 0

    @property
    def peek(self) -> Optional[_T]:
        """Returns the element with the highest priority without removing it. Returns `None` if the queue was empty."""
        return self.heap.peek

    def __bool__(self) -> bool:
        return bool(self.heap)

    def __contains__(self, item: _T) -> bool:
        return item in self.heap

    def __iter__(self) -> Iterator[_T]:
        yield from self.heap


__all__ = ["PriorityQueue"]
