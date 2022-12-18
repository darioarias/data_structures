from __future__ import annotations

from typing import Any, Callable, Generic, Iterable, Optional

from ._protocols import CT
from .nodes import AVLTreeNode as Node


class AVL(Generic[CT]):
    def __init__(self, __items: Optional[Iterable[CT]] = None) -> None:
        self.root: Optional[Node[CT]] = None

        if __items is not None:
            self.root = self.from_iter(__items).root

    def insert(self, value: CT) -> None:
        def insert_helper(node: Optional[Node[CT]], value: CT) -> Node[CT]:
            if node is None:
                return Node(value)

            if value < node:
                node.left = insert_helper(node.left, value)
            else:
                node.right = insert_helper(node.right, value)

            balanced = self._balanced(node)
            balanced.height = max(balanced.left_height, balanced.right_height) + 1
            return balanced

        self.root = insert_helper(self.root, value)


__all__ = ["AVL"]
