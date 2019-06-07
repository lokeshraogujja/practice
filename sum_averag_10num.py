# to accept 10 number and find its sum and average
sum = 0

for i in range(10) :
    num = int(input("Enter a Number : "))
    sum += num
print(f"Sum = {sum} And Average = {sum / 10}")
