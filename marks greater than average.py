# accept 10 marks and display marks which are greater than the average
marks = []
aaveg = []
sum = 0
for i in range(10):
    n = int(input("Enter the Marks of the student : "))
    sum += n
    marks.append(n)
l = len(marks)
avg = sum / l
print(f"The Average Mark is : {avg}")
for i in marks :
    if i >= avg :
        aaveg.append(i)
print(f"The Marks Which are above the Average are : {aaveg} ")
