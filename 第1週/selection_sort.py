def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the list
        min_idx = 0
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = i

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    # Demonstrate the Selection Sort algorithm
    data = [64, 25, 12, 22, 11]
    print(f"Unsorted array: {data}")
    selection_sort(data)
    print(f"Sorted array: {data}")
