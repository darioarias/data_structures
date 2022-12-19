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

    def push(self, value: T) -> None:
        """Adds a value at the front of the list."""
        self._head = SLLNode[T](value, self._head)

        if self._tail is None:
            self._tail = self._head

    def append(self, value: T) -> None:
        """Adds a value at the end of the list."""
        if self._tail is None:
            return self.push(value)

        self._tail.next = SLLNode[T](value)
        self._tail = self._tail.next


__all__ = ["SinglyLinkedList"]
