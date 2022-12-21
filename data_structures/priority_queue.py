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


__all__ = ["PriorityQueue"]
