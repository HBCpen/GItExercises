def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr[i])
    return arr

if __name__ == "__main__":
    # MODIFICATION_POINT_FOR_CONFLICT_EXERCISE
    data1 = [99, 88, 45, 33, 22, 11, 43]
    print("Original array:", data1)
    sorted_data = bubble_sort(data1)
    print("Sorted array:", sorted_data)


