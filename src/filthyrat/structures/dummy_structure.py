"""Dummy structure module used as a starting point for new data structures."""


class DummyStructure:
    """A minimal placeholder data structure.

    This class is intentionally small so it can be replaced or extended
    as real structures are added to the library.
    """

    def __init__(self) -> None:
        self._items: list[object] = []

    def add(self, value: object) -> None:
        """Insert a value into the structure."""
        self._items.append(value)

    def __len__(self) -> int:
        return len(self._items)
