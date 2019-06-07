# accept 10 numbers and place even numbers to right and odd numbers to the left of the list
even = []
odd = []
req = []
for i in range(0,10) :
    n = int(input("Enter a Number : "))
    if n % 2 ==0 :
        even.append(n)
    else :
        odd.append(n)
odd.sort()
even.sort()
odd.extend(even)
req = odd[::]
print(req)
