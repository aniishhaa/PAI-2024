def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
selection_sort(nums)
print("Sorted using Selection Sort:", nums)
