# accept names until user gives end and display them in sorted order without duplicates
names = set()
while True :
    n = input("Enter a Name (press end to stop) : ")
    if n == "end":
        break

    names.add(n)
print(f"The given names are : {sorted(names)}")
