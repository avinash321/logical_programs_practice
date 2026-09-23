lst = [1,2,3,4,5,6]

def get_combinations(lst, start, current):
  for i in range(start, len(lst)):
    current.append(lst[i])
    print(current)
    get_combinations(lst, i+1, current)
    current.pop()

get_combinations(lst, 0, [])
