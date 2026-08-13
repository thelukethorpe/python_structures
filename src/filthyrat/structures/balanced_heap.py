from collections.abc import Callable

type Comparator[T] = Callable[[T, T], int]


class BalancedHeap[T]:
    """A binary heap that maintains balance between the left and right subheaps."""

    def __init__(self, cmp: Comparator[T]) -> None:
        self._top: T | None = None
        self._left: BalancedHeap[T] | None = None
        self._right: BalancedHeap[T] | None = None
        self._cmp = cmp
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def peek(self) -> T | None:
        return self._top

    def add(self, value: T) -> None:
        self._size += 1
        if self._top is None:
            self._top = value
            return

        cmp = self._cmp(value, self._top)
        larger_value: T
        if cmp < 0:
            larger_value = self._top
            self._top = value
        else:
            larger_value = value

        smaller_child: BalancedHeap[T]
        if self._left is None:
            self._left = BalancedHeap[T](self._cmp)
            smaller_child = self._left
        elif self._right is None:
            self._right = BalancedHeap[T](self._cmp)
            smaller_child = self._right
        elif self._left._size < self._right._size:
            smaller_child = self._left
        else:
            smaller_child = self._right

        smaller_child.add(larger_value)
