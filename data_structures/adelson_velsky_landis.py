from __future__ import annotations

from typing import Any, Callable, Generic, Iterable, Optional

from ._protocols import CT
from .nodes import AVLTreeNode as Node


class AVL(Generic[CT]):
    pass


__all__ = ["AVL"]
