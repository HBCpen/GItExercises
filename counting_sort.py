def counting_sort(arr):
    """
    Sorts a list of non-negative integers in ascending order using the Counting Sort algorithm.

    Args:
        arr: The list to be sorted. Assumes non-negative integers.
    """
    if not arr:
        return []

    # Find the maximum element to determine the range of counts
    max_val = arr[0]
    for num in arr:
        if num < 0:
            raise ValueError("Counting Sort only works for non-negative integers.")
        if num > max_val:
            max_val = num

    # Initialize count array with all zeros
    count_len = max_val + 1
    count = [0] * count_len

    # Store count of each character
    for num in arr:
        count[num] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(1, count_len):
        count[i] += count[i - 1]

    # Build the output character array
    output = [0] * len(arr)
    # Iterate in reverse to make it stable
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    # Copy the sorted elements into original array
    for i in range(len(arr)):
        arr[i] = output[i]

if __name__ == "__main__":
    # Demonstrate the Counting Sort algorithm
    data = [4, 2, 2, 8, 3, 3, 1, 0, 7]
    print(f"Unsorted array: {data}")
    counting_sort(data)
    print(f"Sorted array: {data}")

    data_empty = []
    print(f"Unsorted array: {data_empty}")
    counting_sort(data_empty) # Should not modify if empty
    print(f"Sorted array: {data_empty}")

    data_single = [5]
    print(f"Unsorted array: {data_single}")
    counting_sort(data_single)
    print(f"Sorted array: {data_single}")

    data_sorted = [0, 1, 2, 3, 4, 5]
    print(f"Unsorted array: {data_sorted}")
    counting_sort(data_sorted)
    print(f"Sorted array: {data_sorted}")

    # Example with a larger range
    data_large_range = [10, 1, 5, 0, 12, 5]
    print(f"Unsorted array: {data_large_range}")
    counting_sort(data_large_range)
    print(f"Sorted array: {data_large_range}")
