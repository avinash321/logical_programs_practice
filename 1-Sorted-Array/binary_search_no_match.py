# Binary Search
arr = [4, 9, 15, 21, 28, 35, 42, 50, 63, 77]
target = 30

def binary_search(arr, target):
  left  = 0
  right = len(arr) - 1
  while left <= right:
    print(arr[left:right+1])
    mid = (left + right) // 2
    print(mid)
    if arr[mid] < target:
      left = mid + 1
    elif arr[mid] == target:
      return arr[mid]
    else:
      right = mid -1
  return -1


print(binary_search(arr,target))