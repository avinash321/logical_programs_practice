# Find the maximum sum of any two elements
arr = [10, 4, 7, 2, 15, 9]

def find_max_sum(arr):
  first_large = float("-inf")
  second_large = float("-inf")
  for i in arr:
    if i > first_large:
      second_large = first_large
      first_large = i
    elif i > second_large:
      second_large = i
  return first_large + second_large

print(find_max_sum(arr))