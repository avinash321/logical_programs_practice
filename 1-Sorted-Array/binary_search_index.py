# If target exist return its index
# else return -1
arr = [5, 12, 18, 23, 31, 42, 57, 64, 79, 91]
target = 57

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    elif arr[mid] == target:
      return mid
    else:
      right = mid - 1
  return -1

print(binary_search(arr, target))