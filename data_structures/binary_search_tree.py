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


__all__ = ["BinarySearchTree"]
