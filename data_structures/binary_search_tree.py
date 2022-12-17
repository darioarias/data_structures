from __future__ import annotations

from typing import Callable, Generic, Iterable, Optional, Union

from ._protocols import CT
from .nodes import BinarySearchTreeNode as Node


class BinarySearchTree(Generic[CT]):
    pass


__all__ = ["BinarySearchTree"]
