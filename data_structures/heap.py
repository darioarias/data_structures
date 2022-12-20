import operator
import reprlib
from typing import Callable, Generic, Iterator, Optional

from ._protocols import CT


class Heap(Generic[CT]):
    def __init__(
        self,
        __items: Optional[list[CT]] = None,
        heap_type: str = "MIN",
    ) -> None:
        self._elements = []

        self._sort: Callable[[CT, CT], bool]
        try:
            sorters: dict[str, Callable[[CT, CT], bool]] = {
                "min": operator.lt,
                "max": operator.gt,
            }
            self._sort = sorters[heap_type.lower()]
        except:
            raise AttributeError(
                f"Expected Heap type to be either string 'min' or string 'max', instead got <value: {heap_type!r}, type: {type(heap_type).__name__}>"
            )

        if __items is not None:
            self._heapify(__items)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def peek(self) -> Optional[CT]:
        return self._elements[0] if self.size > 0 else None

    def _swap(self, index_a: int, index_b: int) -> None:
        [self._elements[index_a], self._elements[index_b]] = [
            self._elements[index_b],
            self._elements[index_a],
        ]

    def remove(self) -> Optional[CT]:
        if self.is_empty:
            return None

        self._swap(0, self.size - 1)
        min_val = self._elements.pop()

        self._sift_down(0)

        return min_val

    def insert(self, value: CT) -> None:
        self._elements.append(value)
        self._sift_up(self.size - 1)

    def _sift_down(self, from_index: int) -> None:
        _left_child_index: Callable[[int], int] = (
            lambda parent_index: (2 * parent_index) + 1
        )

        _right_child_index: Callable[[int], int] = (
            lambda parent_index: (2 * parent_index) + 2
        )

        parent = from_index
        while True:
            left = _left_child_index(parent)
            right = _right_child_index(parent)

            candidate = parent

            if left < self.size and self._sort(
                self._elements[left], self._elements[candidate]
            ):
                candidate = left

            if right < self.size and self._sort(
                self._elements[right], self._elements[candidate]
            ):
                candidate = right

            if candidate == parent:
                return None

            self._swap(parent, candidate)
            parent = candidate

    def _sift_up(self, from_index: int) -> None:
        _parent_index: Callable[[int], int] = lambda child_index: (child_index - 1) // 2

        child = from_index
        parent = _parent_index(child)
        while child > 0 and self._sort(self._elements[child], self._elements[parent]):
            self._swap(child, parent)
            child = parent
            parent = _parent_index(child)

    def _heapify(self, items: list[CT]) -> None:
        assert isinstance(items, list)
        self._elements = items
        for i in range((len(items) // 2), -1, -1):
            self._sift_down(i)


__all__ = ["Heap"]
