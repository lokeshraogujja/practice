# from the file get details and print them them with marks beside them
f = open("students.txt", "rt")
details = []
students = {}
for det in f:
    details.append(det.split(","))

for n in range(0,len(details)):
    sum = 0
    for i in range(1,len(details[n])):
        if i == len(details[n]) -1:
             details[n][i].strip("\n")
             sum += int(details[n][i])
        else:
             sum += int(details[n][i])
    students[details[n][0]] = sum
for k,v in sorted(students.items()):
    print(f"{k:10s}  {v}")