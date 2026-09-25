arr = [2, 5, 1, 8, 3, 7]

def find_min_sum(arr):
    first_min = float("inf")
    second_min = float("inf")

    for i in arr:
        if i < first_min:
            second_min = first_min
            first_min = i

        elif i < second_min:
            second_min = i

    return first_min + second_min

print(find_min_sum(arr))