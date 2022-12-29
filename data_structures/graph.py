from __future__ import annotations

import enum
import operator
import typing
from collections import defaultdict

from .priority_queue import PriorityQueue

_T = typing.TypeVar("_T")


class _Vertex(typing.Generic[_T]):
    pass
