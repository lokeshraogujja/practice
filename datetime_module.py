# from employee.text display employee details along with experience
import datetime

f = open("employee.txt", "rt")
details = []
for i in f:
    details.append(i.strip("\n").split(","))
