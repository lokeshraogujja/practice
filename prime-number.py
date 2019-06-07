# to tell weather the given number is a prime or not
a = int(input("Enter a Number : "))
for i in range(1, a // 2 + 1):
    if a % i == 0:
        break
if i < a // 2:
    print("Given Number is Not a Prime Number")
else:
    print("Given Number is a Prime Number")
