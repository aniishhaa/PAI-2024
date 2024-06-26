def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_sort(nums)
print("Sorted using Bubble Sort:", nums)
