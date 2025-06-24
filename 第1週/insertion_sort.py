def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    # Demonstrate the Insertion Sort algorithm
    data = [64, 25, 12, 22, 11, 90]
    print(f"Unsorted array: {data}")
    insertion_sort(data)
    print(f"Sorted array: {data}")
