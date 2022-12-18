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

    def remove(self, value: CT) -> None:
        def remove_helper(node: Optional[Node[CT]], value: Any) -> Optional[Node[CT]]:
            if node is None:
                return None

            if value == node:
                if node.left is None and node.right is None:
                    return None
                if node.right is None:
                    return node.left
                if node.left is None:
                    return node.right
                node.value = node.right.min.value
                node.right = remove_helper(node.right, node.value)
            elif value < node:
                node.left = remove_helper(node.left, value)
            else:
                node.right = remove_helper(node.right, value)

            balanced = self._balanced(node)
            balanced.height = max(balanced.left_height, balanced.right_height) + 1
            return balanced

        self.root = remove_helper(self.root, value)

    # Helpers/Private methods

    def _left_rotate(self, node: Node[CT]) -> Node[CT]:
        assert isinstance(node.right, Node)

        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        node.height = max(node.left_height, node.right_height) + 1
        pivot.height = max(pivot.left_height, pivot.right_height) + 1

        return pivot

    def _right_rotate(self, node: Node[CT]) -> Node[CT]:
        assert isinstance(node.left, Node)

        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node.height = max(node.left_height, node.right_height) + 1
        pivot.height = max(pivot.left_height, pivot.right_height) + 1

        return pivot

    def _right_left_rotate(self, node: Node[CT]) -> Node[CT]:
        if node.right is None:
            return node
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def _left_right_rotate(self, node: Node[CT]) -> Node[CT]:
        if node.left is None:
            return node
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)


__all__ = ["AVL"]
