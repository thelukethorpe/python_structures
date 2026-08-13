from filthyrat.structures import BalancedHeap


def ascending_cmp(a: float, b: float) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def test_balanced_heap_add_and_len() -> None:
    bh = BalancedHeap[float](ascending_cmp)
    bh.add(10)
    bh.add(20)

    assert len(bh) == 2


def test_balanced_heap_add_and_peek() -> None:
    bh = BalancedHeap[float](ascending_cmp)
    assert bh.peek() is None

    bh.add(20)
    assert bh.peek() == 20

    bh.add(10)
    assert bh.peek() == 10

    bh.add(15)
    assert bh.peek() == 10

    bh.add(25)
    assert bh.peek() == 10

    bh.add(5)
    assert bh.peek() == 5
