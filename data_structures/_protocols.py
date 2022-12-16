import typing


class Comparable(typing.Protocol):
    def __lt__(self, other: typing.Any, /) -> bool:
        ...

    def __gt__(self, other: typing.Any, /) -> bool:
        ...

    def __eq__(self, other: typing.Any, /) -> bool:
        ...


CT = typing.TypeVar("CT", bound=Comparable)


__all__ = ["CT"]
