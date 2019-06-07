
# take roll numbers and names of the students and diplay them sid eby side

num = []
names = []
while True:
    roll = int(input("Enter the roll number of the student (press 0 to stop) : "))
    if roll == 0 :
        break
    per = input("Enter the name of the student : ")
    num.append(roll)
    names.append(per)
print("Roll Number      Name ")
for i in range(0,len(num)):
     print(f"{num[i]}          {names[i]}")
