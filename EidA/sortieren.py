import random
from typing import List
import timeit


def is_sorted(list: List[int]) -> bool:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def check_sorted(list: List[int], without: bool) -> tuple[bool, List[int]] | bool:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            if without:
                return False
            else:
                return False, list
    if without:
        return True
    else:
        return True, list


def bogo_sort(list: List[int]) -> List[int]:
    while not is_sorted(list):
        random.shuffle(list)

    return list


def bubble_sort(list: List[int], n) -> List[int]:
    for i in range(n - 1):
        for j in range(n, i, -1):
            if list[j] < list[j - 1]:
                tmp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = tmp
    return list


def merge_sort(list: List[int], p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(list, p, q)  # sort left half
    merge_sort(list, q + 1, r)  # sort right half
    return merge(list, p, q, r)  # merge both halves


def merge(list: List[int], p, q, r) -> List[int]:
    n_left = q - p + 1
    n_right = r - q
    left_list, right_list = [], []
    for i in range(n_left):
        left_list.append(list[p + i])
    for j in range(n_right):
        right_list.append(list[q + j + 1])
    i = 0
    j = 0
    k = p
    while i < n_left and j < n_right:
        if left_list[i] <= right_list[j]:
            list[k] = left_list[i]
            i += 1
        else:
            list[k] = right_list[j]
            j += 1
        k += 1
    while i < n_left:
        list[k] = left_list[i]
        i += 1
        k += 1
    while j < n_right:
        list[k] = right_list[j]
        j += 1
        k += 1
    return list


def slow_sort(list: List[int], p, r) -> list[int] | None:
    if p >= r:
        return
    q = (p + r) // 2
    slow_sort(list, p, q)  # sort left half
    slow_sort(list, q + 1, r)  # sort right half
    if list[q] > list[r]:
        tmp = list[q]
        list[q] = list[r]
        list[r] = tmp
    slow_sort(list, p, r - 1)
    return list


def selection_sort(list: List[int], n) -> List[int]:
    for i in range(n + 1):
        min = i
        for j in range(i, n + 1):
            if list[j] < list[min] and j != min:
                min = j
            list[i], list[min] = list[min], list[i]
    return list


# TODO: heap sort
def heap_sort(list: List[int], n) -> List[int]:
    pass


# TODO: pivot functions
def quick_sort(list: List[int], pivot_func):
    l, p, r = partition(list, pivot_func(list))

    if len(l) > 1:
        l = quick_sort(l, pivot_func)
    if len(r) > 1:
        r = quick_sort(r, pivot_func)

    # join lists
    return l + p + r


def partition(list: List[int], pivot):
    arr_left, arr_right = [], []
    for i in range(len(list)):
        if i == pivot:
            continue
        if list[i] < list[pivot]:
            arr_left.append(list[i])
        else:
            arr_right.append(list[i])

    return arr_left, [list[pivot]], arr_right


def pivot_first(list: List[int]) -> int:
    return 0


# TODO: bucket sort
def bucket_sort(list: List[int], n) -> List[int]:
    pass


# TODO: radix sort
def radix_sort(list: List[int], n) -> List[int]:
    pass


# TODO: counting sort
def counting_sort(list: List[int], n, k) -> List[int]:
    pass


if __name__ == '__main__':
    n = 1  # number of timeit iterations
    without = True  # True if you want the list NOT printed with check_sorted()
    n_e = 10  # number of elements in list
    list = [random.randint(0, n_e) for i in range(n_e)]

    print('Unsorted:', check_sorted(list[:], False))
    bubble_time = timeit.timeit(stmt='bubble_sort(list[:], len(list) - 1)', globals=globals(), number=n)
    print('Bubble Sort:', check_sorted(bubble_sort(list[:], len(list) - 1), False), bubble_time / n)
    list = [random.randint(0, n_e) for i in range(n_e)]
    selection_time = timeit.timeit(stmt='selection_sort(list[:], len(list) - 1)', globals=globals(), number=n)
    print('Selection Sort', check_sorted(selection_sort(list[:], len(list) - 1), False), selection_time / n)
    list = [random.randint(0, n_e) for i in range(n_e)]
    bogo_time = timeit.timeit(stmt='bogo_sort(list[:])', globals=globals(), number=n)
    print('Bogo Sort', check_sorted(bogo_sort(list[:]), False), bogo_time / n)
    list = [random.randint(0, n_e) for i in range(n_e)]
    quick_time = timeit.timeit(stmt='quick_sort(list[:], pivot_first)', globals=globals(), number=n)
    print('Quick Sort', check_sorted(quick_sort(list[:], pivot_first), False), quick_time / n)
    list = [random.randint(0, n_e) for i in range(n_e)]
    merge_time = timeit.timeit(stmt='merge_sort(list[:], 0, len(list) - 1)', globals=globals(), number=n)
    print('Merge Sort', check_sorted(merge_sort(list[:], 0, len(list) - 1), False), merge_time / n)
    list = [random.randint(0, n_e) for i in range(n_e)]
    slow_time = timeit.timeit(stmt='slow_sort(list[:], 0, len(list) - 1)', globals=globals(), number=n)
    print('Slow Sort', check_sorted(slow_sort(list[:], 0, len(list) - 1), False), slow_time / n)
