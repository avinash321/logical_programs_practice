intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

previous = intervals[0]
result = []

for i in range(1, len(intervals)):
    current = intervals[i]
    if current[0] <= previous[-1]:
        low_range = min(previous[0],current[0])
        high_range = max(previous[-1],current[-1])
        previous = [low_range, high_range]
    else:
        result.append(previous)
        previous = current
result.append(previous)

print(result)