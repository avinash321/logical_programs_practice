num = int(input("Enter Your Number: "))
counter = 0
if num <=1:
    print(f"Given Number {num} Not a Prime number")
for i in range(2, int(num/2 +1)):
    if num % i == 0:
        counter += 1

if not counter:
    print(f"Give Number {num} is Prime Number")
else:
    print(f"Give Number {num} is Not Prime Number")
    