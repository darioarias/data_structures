from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar, Union

from ._protocols import CT

T = TypeVar("T")


class BinarySearchTreeNode(Generic[CT]):
    def __init__(
        self,
        value: CT,
        left: Optional[BinarySearchTreeNode[CT]] = None,
        right: Optional[BinarySearchTreeNode[CT]] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    # overloading props to comply with leetcode
    @property
    def val(self) -> CT:
        return self.value

    @val.setter
    def val(self, value: CT) -> None:
        self.value = value

    @property
    def min(self) -> BinarySearchTreeNode[CT]:
        """Recursively selects the node with the minimun value starting from a given node."""
        if self.left is None:
            return self
        return self.left.min

    def __iter__(self) -> Iterator[Union[CT, BinarySearchTreeNode[CT] | None]]:
        yield from (self.value, self.left, self.right)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value!r})"

    def __str__(self) -> str:
        return f"{str(self.val)}"

    def __lt__(self, __o: Union[CT, BinarySearchTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, BinarySearchTreeNode):
                return self.value < __o.value
            return self.value < __o
        except TypeError:
            return NotImplemented

    def __eq__(self, __o: Union[CT, BinarySearchTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, BinarySearchTreeNode):
                return self.value == __o.value
            return self.value == __o
        except TypeError:
            return NotImplemented

    def __gt__(self, __o: Union[CT, BinarySearchTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, BinarySearchTreeNode):
                return self.value > __o.value
            return self.value > __o
        except TypeError:
            return NotImplemented


class AVLTreeNode(Generic[CT]):
    def __init__(
        self,
        value: CT,
        left: Optional[AVLTreeNode[CT]] = None,
        right: Optional[AVLTreeNode[CT]] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.height = 0

    @property
    def val(self) -> CT:
        return self.value

    @val.setter
    def val(self, value: CT) -> None:
        self.value = value

    @property
    def left_height(self) -> int:
        if self.left is not None:
            return self.left.height
        return -1

    @property
    def right_height(self) -> int:
        if self.right is not None:
            return self.right.height
        return -1

    @property
    def balance_factor(self) -> int:
        return self.left_height - self.right_height

    @property
    def min(self) -> AVLTreeNode[CT]:
        if self.left is None:
            return self
        return self.left.min

    def __eq__(self, __o: Union[CT, AVLTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, AVLTreeNode):
                return self.value == __o.value
            return self.value == __o
        except TypeError:
            return NotImplemented

    def __lt__(self, __o: Union[CT, AVLTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, AVLTreeNode):
                return self.value < __o.value
            return self.value < __o
        except TypeError:
            return NotImplemented

    def __gt__(self, __o: Union[CT, AVLTreeNode[CT]]) -> bool:
        try:
            if isinstance(__o, AVLTreeNode):
                return self.value > __o.value
            return self.value > __o
        except TypeError:
            return NotImplemented

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value!r})"

    def __str__(self) -> str:
        return f"{str(self.value)}"

    def __iter__(self) -> Iterator[Union[CT, AVLTreeNode[CT] | None]]:
        yield from (self.value, self.left, self.right)


class SinglyLinkedListNode(tuple[T, "SinglyLinkedListNode[T]"]):
    def __new__(
        cls, value: T, next: Optional[SinglyLinkedListNode[T]] = None
    ) -> SinglyLinkedListNode[T]:
        return tuple.__new__(cls, (value, next))

    def __init__(
        self, value: T, next: Optional[SinglyLinkedListNode[T]] = None
    ) -> None:
        self.value = value
        self.next = next

    @property
    def val(self) -> T:
        return self.value

    @val.setter
    def val(self, value: T) -> None:
        self.value = value

    def __iter__(self) -> Iterator[Union[T, Optional[SinglyLinkedListNode[T]]]]:
        yield from (self.value, self.next)

    def __eq__(self, __o: Union[T, SinglyLinkedListNode[T]]) -> bool:
        try:
            if isinstance(__o, SinglyLinkedListNode):
                return self.value == __o.value
            return self.value == __o
        except TypeError:
            raise NotImplemented

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.val!r})"

    def __str__(self) -> str:
        return f"{str(self.value)}"


class DoublyLinkedListNode(
    tuple[T, "DoublyLinkedListNode[T]", "DoublyLinkedListNode[T]"]
):
    def __new__(
        cls,
        value: T,
        next: Optional[DoublyLinkedListNode[T]] = None,
        previous: Optional[DoublyLinkedListNode[T]] = None,
    ) -> DoublyLinkedListNode[T]:
        return tuple.__new__(cls, (value, next, previous))

    def __init__(
        self,
        value: T,
        next: Optional[DoublyLinkedListNode[T]] = None,
        previous: Optional[DoublyLinkedListNode[T]] = None,
    ) -> None:
        self.value = value
        self.next = next
        self.previous = previous

    @property
    def val(self) -> T:
        return self.value

    @val.setter
    def val(self, value: T) -> None:
        self.value = value

    @property
    def prev(self) -> Optional[DoublyLinkedListNode[T]]:
        return self.previous

    @prev.setter
    def prev(self, value: Optional[DoublyLinkedListNode[T]]) -> None:
        self.previous = value

    def __iter__(self) -> Iterator[Union[T, Optional[DoublyLinkedListNode[T]]]]:
        yield from (self.value, self.next, self.previous)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value!r})"

    def __str__(self) -> str:
        return f"{str(self.value)}"

    def __eq__(self, __o: Union[T, DoublyLinkedListNode[T]]) -> bool:
        try:
            if isinstance(__o, DoublyLinkedListNode):
                return self.value == __o.value
            return self.value == __o
        except TypeError:
            raise NotImplemented


__all__ = [
    "BinarySearchTreeNode",
    "AVLTreeNode",
    "SinglyLinkedListNode",
    "DoublyLinkedListNode",
]
