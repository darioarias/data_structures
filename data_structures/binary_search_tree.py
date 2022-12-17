from __future__ import annotations

from typing import Callable, Generic, Iterable, Optional, Union

from ._protocols import CT
from .nodes import BinarySearchTreeNode as Node


class BinarySearchTree(Generic[CT]):
    def __init__(self, __items: Optional[Iterable[CT]] = None) -> None:
        self.root: Optional[Node[CT]] = None

        if __items is not None:
            self.root = self.from_iter(__items).root
            return None

    def insert(self, value: CT) -> None:
        """Inserts a value into the tree"""

        def insert_helper(root: Optional[Node[CT]], value: CT) -> Node[CT]:
            if root is None:
                return Node[CT](value)
            if value < root:
                root.left = insert_helper(root.left, value)
            else:
                root.right = insert_helper(root.right, value)
            return root

        self.root = insert_helper(self.root, value)


__all__ = ["BinarySearchTree"]
