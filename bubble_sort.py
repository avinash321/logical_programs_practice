lst = [5, 2, 4, 8, 1]

# bubble sorting
for i in range(len(lst)):
  for j in range(0, len(lst)-i-1):
    if lst[j] > lst[j+1]:
      lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)