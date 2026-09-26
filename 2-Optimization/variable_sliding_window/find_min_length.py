arr = [2, 1, 5, 2, 3, 2]
target = 7

left = 0
current_sum = 0
min_length = float("inf")

for right in range(len(arr)):
    # Expand the window
    current_sum += arr[right]
    # Shrink the window while it is valid
    while current_sum >= target:

        # Record the current window length
        min_length = min(min_length, right - left + 1)

        # Remove the left element
        current_sum -= arr[left]
        left += 1

# If no valid window was found
if min_length == float("inf"):
    print(0)
else:
    print(min_length)