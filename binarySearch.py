def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1, 3, 4, 5, 5, 6, 9]
target = 6
index = binary_search(nums, target)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")
