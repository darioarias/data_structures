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


__all__ = ["Heap"]
