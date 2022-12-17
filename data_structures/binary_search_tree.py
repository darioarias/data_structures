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

    @staticmethod
    def from_mapped_list(items: list[Union[CT, None]]) -> BinarySearchTree[CT]:
        """Uses indexies to creat a tree from a list.
        This algorithms assumes that values are already in the correct order.
        """
        left_child: Callable[[int], int] = lambda index: 2 * index + 1
        right_child: Callable[[int], int] = lambda index: 2 * index + 2

        def construct_tree(
            items: list[Union[CT, None]], index: int
        ) -> Optional[Node[CT]]:
            if index >= len(items):
                return None

            item = items[index]
            if item is None:
                return None

            root: Node[CT] = Node(item)
            root.left = construct_tree(items, left_child(index))
            root.right = construct_tree(items, right_child(index))

            return root

        _temp_bst: BinarySearchTree[CT] = BinarySearchTree()
        _temp_bst.root = construct_tree(items, 0)
        return _temp_bst

    @staticmethod
    def from_iter(items: Iterable[CT]) -> BinarySearchTree[CT]:
        """Uses the builtin insert method to create a tree from an iterable"""
        _temp_bst = BinarySearchTree[CT]()
        for item in items:
            _temp_bst.insert(item)

        return _temp_bst

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

    def remove(self, value: CT) -> None:
        """Removes a given value from the tree"""

        def remove_helper(root: Optional[Node[CT]], value: CT) -> Optional[Node[CT]]:
            if root is None:
                return None

            if root == value:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                root.value = root.right.min.value
                root.right = remove_helper(root.right, root.value)
            elif value < root:
                root.left = remove_helper(root.left, value)
            else:
                root.right = remove_helper(root.right, value)
            return root

        self.root = remove_helper(self.root, value)

    def __contains__(self, item: CT) -> bool:
        def contains(root: Optional[Node[CT]], value: CT) -> bool:
            if root is None:
                return False
            if root.value == value:
                return True
            if root < value:
                return contains(root.right, value)
            else:
                return contains(root.left, value)

        return contains(self.root, item)

    def __str__(self) -> str:
        def diagram(
            node: Optional[Node[CT]], top: str = "", root: str = "", bottom: str = ""
        ) -> str:
            """This algorithm is based on an implementation by Károly Lőrentey in his book [Optimizing Collections](https://www.objc.io/books/optimizing-collections/)"""
            if node is None:
                return root + "None\n"
            if node.left is None and node.right is None:
                return root + f"{node.value!r}\n"
            return (
                diagram(node.right, top + "  ", top + "┌─", top + "│ ")
                + root
                + f"{node.value!r}\n"
                + diagram(node.left, bottom + "│ ", bottom + "└─", bottom + "  ")
            )

        return diagram(self.root)


__all__ = ["BinarySearchTree"]
