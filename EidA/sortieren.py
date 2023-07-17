import random
from typing import List, Tuple


def is_sorted(list: List[int]) -> bool:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def check_sorted(list: List[int]) -> tuple[bool, List[int]]:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False, list
    return True, list


def bogosort(list: List[int]) -> List[int]:
    while not is_sorted(list):
        random.shuffle(list)
    return list


def bubblesort(list: List[int], n) -> List[int]:
    for i in range(n - 1):
        for j in range(n, i, -1):
            if list[j] < list[j - 1]:
                tmp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = tmp
    return list


def mergesort(list: List[int], p, r):
    if p >= r:
        return
    q = (p + r) // 2
    mergesort(list, p, q)  # sort left half
    mergesort(list, q + 1, r)  # sort right half
    return merge(list, p, q, r)  # merge both halves


def merge(list: List[int], p, q, r):
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


def slowsort(list: List[int], p, r) -> list[int] | None:
    if p >= r:
        return
    q = (p + r) // 2
    slowsort(list, p, q)  # sort left half
    slowsort(list, q + 1, r)  # sort right half
    if list[q] > list[r]:
        tmp = list[q]
        list[q] = list[r]
        list[r] = tmp
    slowsort(list, p, r - 1)
    return list


def selectionsort(list: List[int], n) -> List[int]:
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
            tmp = list[i]
            list[i] = list[min]
            list[min] = tmp
    return list


# TODO: heap sort
def heapsort(list: List[int], n) -> List[int]:
    pass


# TODO: pivot functions
def quicksort(list: List[int], pivot_func):
    l, p, r = partition(list, pivot_func(list))

    if len(l) > 1:
        l = quicksort(l, pivot_func)
    if len(r) > 1:
        r = quicksort(r, pivot_func)

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
def bucketsort(list: List[int], n) -> List[int]:
    pass


# TODO: radix sort
def radixsort(list: List[int], n) -> List[int]:
    pass


# TODO: counting sort
def countingSort(list: List[int], n, k) -> List[int]:
    pass


if __name__ == '__main__':
    list = [random.randint(0, 100) for i in range(10)]
    print('Unsorted:', check_sorted(list))
    print('Bubble Sort:', check_sorted(bubblesort(list, len(list) - 1)))
    print('Selection Sort', check_sorted(selectionsort(list, len(list) - 1)))
    print('Bogo Sort', check_sorted(bogosort(list)))
    print('Quick Sort', check_sorted(quicksort(list, pivot_first)))
    print('Merge Sort', check_sorted(mergesort(list, 0, len(list) - 1)))
    print('Slow Sort', check_sorted(slowsort(list, 0, len(list) - 1)))
