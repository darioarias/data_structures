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

    def insert(self, after: SLLNode, value: T) -> None:
        """Adds a value after a particular list node."""
        assert isinstance(after, SLLNode), "After must be a Node"

        if after is self._tail:
            return self.append(value)

        _, next = after
        after.next = SLLNode[T](value, next)

    def pop(self) -> typing.Optional[T]:
        """Removes the value at the front of the list."""
        if self._head is None:
            return None

        value, next = self._head

        self._head = next

        if self._head is None:
            self._tail = None

        return value

    def remove_last(self) -> typing.Optional[T]:
        """Removes the value at the end of the list."""
        if self._tail is None:
            return None

        if self._tail is self._head:
            return self.pop()

        before_tail: typing.Optional[SLLNode] = None
        for node in self:
            if node.next is self._tail:
                before_tail = node
                break

        assert isinstance(
            before_tail, SLLNode
        ), "the node before tail should always be of type Node"

        value, _ = self._tail
        before_tail.next = None
        self._tail = before_tail
        return value


__all__ = ["SinglyLinkedList"]
