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


__all__ = ["Heap"]
