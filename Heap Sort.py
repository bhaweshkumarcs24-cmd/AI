def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        for j in range(i, -1, -1):
            largest = j
            left = 2 * j + 1
            right = 2 * j + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            arr[j], arr[largest] = arr[largest], arr[j]

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Sorted array:", arr)
