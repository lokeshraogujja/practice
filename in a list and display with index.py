# take a list of values and display them with index
num = []
while True:
    n = int(input("Enter a Number (type 0 to stop) : "))
    if n == 0 :
        break
    num.append(n)

l = len(num)
for i in range(0,l):
    print(f"num[{i}] = {num[i]} ")




