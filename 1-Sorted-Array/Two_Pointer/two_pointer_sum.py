arr = [1, 2, 4, 6, 8, 9, 11, 15]
target_sum = 13

def two_pointer_sum(arr, target_sum):
  left = 0
  right = len(arr) - 1
  while left <= right:
    current_sum = arr[left] + arr[right]
    if current_sum < target_sum:
      left += 1
    elif current_sum == target_sum:
      return arr[left], arr[right]
    else:
      right -= 1

print(two_pointer_sum(arr,target_sum))