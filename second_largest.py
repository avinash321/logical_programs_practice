l = [10,2,3,67,77,101,23,34]
first_max = 0
second_max = 0
for i in l:
    if i > first_max:
        second_max = first_max
        first_max = i
print(f"First largest number is {first_max}")
print(f"Second largest number is {second_max}")