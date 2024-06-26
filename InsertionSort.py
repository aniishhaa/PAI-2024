def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
insertion_sort(nums)
print("Sorted using Insertion Sort:", nums)
