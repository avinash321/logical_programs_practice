# Single Pass Linear Scan  O(n)
# Counter Tracking Pattern
# State-Based Traversal
# "Single-pass linear scan using state tracking"

num = 10010001
max_count = 0
temp_count = 0
seen_one = False

for char in str(num):
  if char == "1":
    if seen_one:
      max_count = max(max_count, temp_count)
    seen_one = True
    temp_count = 0
  else:
    if seen_one:
      temp_count += 1
      
print(max_count)