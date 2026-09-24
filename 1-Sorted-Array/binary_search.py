arr = [3, 7, 12, 18, 25, 31, 42, 56, 71, 89]
target = 42

def binary_search(arr, target):
  left = 0
  right = len(arr) -1
  while left <= right:
    mid = (left + right) //2
    if arr[mid] < target:
      left = mid +1
    elif arr[mid] == target:
      return f"{target} present in the Array"
    else:
      right = mid -1


print(binary_search(arr, target))