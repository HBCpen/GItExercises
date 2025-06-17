def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    # MODIFICATION_POINT_FOR_CONFLICT_EXERCISE
    data = [64, 34, 25, 12, 22, 11, 90]
    data_2 = [74,78,82,84,92.5,93,100]
    print("Original array:", data)
    sorted_data = bubble_sort(data)
    print("Sorted array:", sorted_data)

