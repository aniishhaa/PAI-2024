def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 6
index = linear_search(nums, target)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")
