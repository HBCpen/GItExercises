def partition(arr, low, high):
    """
    Helper function to find the partition position.
    Selects the last element as pivot and places it at its correct position
    in sorted array, and places all smaller (smaller than pivot) to left of
    pivot and all greater elements to right of pivot.
    """
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for greater element

    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the position from where partition is done


def quick_sort_recursive(arr, low, high):
    """
    Recursive function to perform Quick Sort.
    """
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursive call on the left of pivot
        quick_sort_recursive(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort_recursive(arr, pi + 1, high)


def quick_sort(arr):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    quick_sort_recursive(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    # Demonstrate the Quick Sort algorithm
    data = [64, 25, 12, 22, 11, 90, 34, 7]
    print(f"Unsorted array: {data}")
    quick_sort(data)
    print(f"Sorted array: {data}")
