from __future__ import annotations

import typing

from .nodes import SinglyLinkedListNode as SLLNode

T = typing.TypeVar("T")


class SinglyLinkedList(typing.Generic[T]):
    def __init__(self, __items: typing.Optional[typing.Iterable[T]] = None) -> None:
        self._head: typing.Optional[SLLNode[T]] = None
        self._tail: typing.Optional[SLLNode[T]] = None

        if __items is not None:
            for item in __items:
                self.append(item)


__all__ = ["SinglyLinkedList"]
