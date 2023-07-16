import random
from typing import List, Tuple


def is_sorted(list: List[int]) -> bool:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def bogosort(list: List[int]) -> List[int]:
    while not isSorted(list):
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


# TODO: merge sort
def mergesort(list: List[int], p, r) -> List[int]:
    pass


def merge():
    pass


# TODO: slow sort
def slowsort(list: List[int], p, r) -> List[int]:
    pass


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


# TODO: quick sort
def quicksort(list: List[int], p, r) -> List[int]:
    pass


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
    print(list)
    print(bubblesort(list, len(list) - 1))
    print(selectionsort(list, len(list) - 1))
    print(bogosort(list))
    print("sortieren")
