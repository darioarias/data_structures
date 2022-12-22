from __future__ import annotations

import typing

from .nodes import DoublyLinkedListNode as DLLNode
from .nodes import SinglyLinkedListNode as SLLNode

T = typing.TypeVar("T")


class SinglyLinkedList(typing.Generic[T]):
    def __init__(self, __items: typing.Optional[typing.Iterable[T]] = None) -> None:
        self._head: typing.Optional[SLLNode[T]] = None
        self._tail: typing.Optional[SLLNode[T]] = None

        if __items is not None:
            for item in __items:
                self.append(item)

    @staticmethod
    def print_from(head: SLLNode[typing.Any]) -> None:
        def gen(head: typing.Optional[SLLNode[typing.Any]]) -> typing.Iterator[str]:
            while head:
                yield str(head)
                head = head.next

        assert head is not None, "A starting node must be provided."
        print(" -> ".join(gen(head)))

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

    def remove(self, after: SLLNode[T]) -> typing.Optional[T]:
        """Removes a value anywhere in the list."""
        assert isinstance(after, SLLNode), "After must be of type Node"

        if after.next is None:
            return None

        if after.next is self._tail:
            return self.remove_last()

        value, next = after.next

        after.next = next
        return value

    def __iter__(self) -> typing.Iterator[SLLNode[T]]:
        current = self._head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return " -> ".join(repr(node) for node in self)

    def __str__(self) -> str:
        return " -> ".join(str(node) for node in self)

    def __contains__(self, value: T) -> bool:
        for node_val, _ in self:
            if node_val == value:
                return True
        return False

    def __reversed__(self) -> typing.Iterator[SLLNode[T]]:
        def _empt_itr() -> typing.Iterator[SLLNode[T]]:
            yield from ()

        def _reverse(node: SLLNode[T]) -> typing.Iterator[SLLNode[T]]:
            if node.next is None:
                yield node
            else:
                yield from _reverse(node.next)
                yield node

        if self._head is None:
            return _empt_itr()
        return _reverse(self._head)

    def __bool__(self) -> bool:
        if self._head is None:
            return False
        return True


class DoublyLinkedList(typing.Generic[T]):
    def __init__(self, __items: typing.Optional[typing.Iterable[T]] = None) -> None:
        self._head: typing.Optional[DLLNode[T]] = None
        self._tail: typing.Optional[DLLNode[T]] = None

        if __items is not None:
            for item in __items:
                self.append(item)

    def push(self, value: T) -> None:
        """Adds a value at the front of the list."""
        self._head = DLLNode[T](value, self._head)

        if self._head.next is not None:
            self._head.next.previous = self._head

        if self._tail is None:
            self._tail = self._head

    def append(self, value: T) -> None:
        """Adds a value at the end of the list."""
        if self._tail is None:
            return self.push(value)

        self._tail = DLLNode[T](value, None, self._tail)

        assert isinstance(self._tail.previous, DLLNode)
        self._tail.previous.next = self._tail

    def insert(self, after: DLLNode[T], value: T) -> None:
        """Adds a value after a particular list node."""
        assert isinstance(after, DLLNode), "after must be of type Node"

        if after is self._tail:
            return self.append(value)

        _, next, _ = after
        # assert isinstance(next, DLLNode)
        after.next = DLLNode[T](value, next, after)
        next.previous = after.next

    def pop(self) -> typing.Optional[T]:
        """Removes the value at the front of the list."""
        if self._head is None:
            return None

        value, next, _ = self._head
        if self._head is self._tail:
            self._head = None
            self._tail = None
            return value

        # assert isinstance(next, DLLNode), "next will always be of type Node"
        next.previous = None

        self._head = next
        return value

    def remove_last(self) -> typing.Optional[T]:
        """Removes the value at the end of the list."""
        if self._tail is None:
            return None

        if self._tail is self._head:
            return self.pop()

        value, _, prev = self._tail

        # assert isinstance(prev, DLLNode)
        prev.next = None

        self._tail = prev
        return value

    def remove(self, after: DLLNode[T]) -> typing.Optional[T]:
        """Removes a value anywhere in the list."""
        assert isinstance(after, DLLNode), "after must be of type Node"

        if after.next is None:
            return None

        if after.next is self._tail:
            return self.remove_last()

        _, next, _ = after
        # assert isinstance(next, DLLNode)

        after.next = next.next

        assert isinstance(after.next, DLLNode)
        after.next.prev = after
        return next.value

    def __iter__(self) -> typing.Iterator[DLLNode[T]]:
        current = self._head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return " <-> ".join(repr(node) for node in self)

    def __str__(self) -> str:
        return " <-> ".join(str(node) for node in self)

    def __contains__(self, __item: T) -> bool:
        for node in self:
            if node == __item:
                return True
        return False

    def __reversed__(self) -> typing.Iterator[DLLNode[T]]:
        current = self._tail
        while current:
            yield current
            current = current.previous

    def __bool__(self) -> bool:
        if self._head is None:
            return False
        return True


__all__ = ["SinglyLinkedList", "DoublyLinkedList"]
