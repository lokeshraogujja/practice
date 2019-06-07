# use filter function to separate prime numbers
def prime(num):
    for n in range(2,num // 2 + 1):
        if num % n == 0:
            break
    if n <= num // 2:
        return False
    else :
        return True
    del(n)




nums = []
while True :
    m = int(input("Enter a Number (press 0 to stop): "))
    if m == 0:
        break
    nums.append(m)


for l in filter(prime,nums):
    print(l)
    