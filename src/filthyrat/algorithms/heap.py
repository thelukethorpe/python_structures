from typing import Any


def bottom_up_heapify(values: list[int]) -> None:
    num_values = len(values)
    parent = (num_values >> 1) - 1
    left_child = (parent << 1) + 1
    right_child = left_child + 1
    while parent >= 0:
        sift_down(values, parent)
        parent -= 1
        left_child -= 2
        right_child -= 2


def sift_down(values: list[int], i: int) -> None:
    num_values = len(values)
    parent = i
    num_parents = num_values >> 1
    while parent < num_parents:
        left_child = (parent << 1) + 1
        right_child = left_child + 1
        swap_candidate = left_child
        if right_child < num_values and values[right_child] < values[left_child]:
            swap_candidate = right_child
        if values[swap_candidate] < values[parent]:
            swap(values, swap_candidate, parent)
            parent = swap_candidate
        else:
            return


def swap(values: list[Any], i: int, j: int) -> None:
    temp = values[i]
    values[i] = values[j]
    values[j] = temp
