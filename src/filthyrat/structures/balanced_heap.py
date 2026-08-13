from collections.abc import Callable
from typing import cast

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

        larger_value: T
        if self._cmp(value, self._top) < 0:
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

    def pop(self) -> T | None:
        if self._top is None:
            return None

        self._size -= 1
        top = self._top
        child_with_smaller_top: BalancedHeap[T] | None
        if self._left is None:
            child_with_smaller_top = self._right
        elif self._right is None:
            child_with_smaller_top = self._left
        elif self._cmp(cast(T, self._left._top), cast(T, self._right._top)) < 0:
            child_with_smaller_top = self._left
        else:
            child_with_smaller_top = self._right

        if child_with_smaller_top is None:
            self._top = None
            return top

        self._top = child_with_smaller_top.pop()

        child_with_larger_top: BalancedHeap[T] | None
        if child_with_smaller_top == self._left:
            child_with_larger_top = self._right
        else:
            child_with_larger_top = self._left

        # TODO prune children
        # TODO double check
        # TODO is there a cleaner approach? (intermediate nodes, but less efficient - maybe on_empty callback)
        # TODO test

        if child_with_larger_top is None:
            return top

        # Rotate
        if child_with_smaller_top._size - child_with_larger_top._size > 1:
            top_to_rotate = cast(T, child_with_smaller_top.pop())
            child_with_larger_top.add(top_to_rotate)
        elif child_with_larger_top._size - child_with_smaller_top._size > 1:
            top_to_rotate = cast(T, child_with_larger_top.pop())
            child_with_smaller_top.add(top_to_rotate)

        return top
