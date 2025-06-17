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
    data = [5, 6, 3, 5, 1, 9, 8]
    data2 = [8, 7, 4, 3, 2]
    print("Original array:", data2)
    sorted_data = bubble_sort(data2)
    print("Sorted array:", sorted_data)


