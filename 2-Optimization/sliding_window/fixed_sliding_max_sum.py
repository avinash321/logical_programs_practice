# Find the maximum sum of any k consecutive elements

arr = [2, 1, 5, 1, 3, 2]
k = 3

initial_window = arr[0:k]
current_sum = sum(initial_window)
max_sum = current_sum

for i in range(len(arr) - k):
    current_sum = current_sum - arr[i] + arr[i + k]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)