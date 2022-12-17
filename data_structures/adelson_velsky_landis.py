from __future__ import annotations

from typing import Any, Callable, Generic, Iterable, Optional

from ._protocols import CT
from .nodes import AVLTreeNode as Node


class AVL(Generic[CT]):
    def __init__(self, __items: Optional[Iterable[CT]] = None) -> None:
        self.root: Optional[Node[CT]] = None

        if __items is not None:
            self.root = self.from_iter(__items).root


__all__ = ["AVL"]
