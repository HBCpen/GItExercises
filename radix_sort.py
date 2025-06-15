def counting_sort_for_radix(arr, exp):
    """
    Helper function to perform counting sort on arr[] according to
    the digit represented by exp (exponent, e.g., 1, 10, 100).
    Assumes non-negative integers.
    """
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # Digits 0-9

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers according to current digit
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Sorts a list of non-negative integers in ascending order using the Radix Sort algorithm.

    Args:
        arr: The list to be sorted. Assumes non-negative integers.
    """
    if not arr:
        return

    # Find the maximum number to know number of digits
    max_val = arr[0]
    for num in arr:
        if num < 0:
            raise ValueError("Radix Sort only works for non-negative integers.")
        if num > max_val:
            max_val = num

    if max_val == 0 and all(x == 0 for x in arr): # Handle array of all zeros
        return


    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

if __name__ == "__main__":
    # Demonstrate the Radix Sort algorithm
    data1 = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Unsorted array: {data1}")
    radix_sort(data1)
    print(f"Sorted array: {data1}")

    data2 = [4, 2, 2, 8, 3, 3, 1, 0, 7]
    print(f"Unsorted array: {data2}")
    radix_sort(data2)
    print(f"Sorted array: {data2}")

    data_empty = []
    print(f"Unsorted array: {data_empty}")
    radix_sort(data_empty)
    print(f"Sorted array: {data_empty}")

    data_single = [5]
    print(f"Unsorted array: {data_single}")
    radix_sort(data_single)
    print(f"Sorted array: {data_single}")

    data_sorted = [0, 1, 2, 3, 4, 5]
    print(f"Unsorted array: {data_sorted}")
    radix_sort(data_sorted)
    print(f"Sorted array: {data_sorted}")

    data_all_zeros = [0, 0, 0, 0]
    print(f"Unsorted array: {data_all_zeros}")
    radix_sort(data_all_zeros)
    print(f"Sorted array: {data_all_zeros}")

    data_large_numbers = [12345, 678, 90, 1, 5432]
    print(f"Unsorted array: {data_large_numbers}")
    radix_sort(data_large_numbers)
    print(f"Sorted array: {data_large_numbers}")
