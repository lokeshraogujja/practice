# accept numbers untill zero is given and find the sum and average of the given numbers
sum = 0
count = 0
while True:
     num = int(input("Enter a Number : "))
     if num == 0:
        break
     sum += num
     count += 1
print(f"Sum = {sum} and average = {sum/count}")

