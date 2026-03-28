# Q: Find the maximum sum of any subarray of size k (OR)
# Q: Find the maximum sum of k consecutive elements
# fixed-size sliding window
arr = [2, 1, 5, 1, 3, 2]
k = 3

# Initial window calculated once
window = arr[:k]
window_sum = sum(window)
max_sum = window_sum

#left = 0 
# Loopingarr[k:right+1] & incrementing left
# Reusing previously caliculated window_sum
for right in range(k, len(arr)):
  # Reusing window_sum
  # Adding incoming + removing outgoing element
  # instead of - arr[left] we can use arr[right-k]
  window_sum = window_sum + arr[right] - arr[right-k]
  # Tracking max_sum
  max_sum = max(max_sum, window_sum)
  #left += 1
  
# O(n) time with O(1) updates
print(max_sum)
