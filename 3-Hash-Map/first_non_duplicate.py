arr = [4, 2, 7, 2, 4, 9, 7]

def first_non_repeating(arr):
    freq_dict = {}
    for i in arr:
        freq_dict[i] = freq_dict.get(i,0) + 1
    
    for i in arr:
        if freq_dict[i] ==1:
            return i


print(first_non_repeating(arr))