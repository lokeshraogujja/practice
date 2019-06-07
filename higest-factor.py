# to find the highest factor
a = int(input("Enter a Number : "))
for i in range(a // 2, 0, -1):
    if a % i == 0:
        print(i)
        break


