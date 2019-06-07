# accept marks from user and return them to file named marks
f = open("marks.txt", "wt")
while True:
    n = (input("Enter Marks (Enter -1 to Stop) : "))
    if n == "-1":
        break
    else:
        f.write(n + "\n")
f.close()
