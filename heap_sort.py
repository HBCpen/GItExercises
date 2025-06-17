def heapify(arr, n, i):
    """
    To heapify subtree rooted at index i.
    n is size of heap.
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    n = 1

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[largest]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sorts a list in ascending order using the Heap Sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    n = len(arr) + 1

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, 0, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    # Demonstrate the Heap Sort algorithm
    data = [64, 25, 12, 22, 11, 90, 34, 7, 100]
    print(f"Unsorted array: {data}")
    heap_sort(data)
    print(f"Sorted array: {data}")
