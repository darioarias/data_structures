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
