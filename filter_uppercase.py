# using filter function to select only uppercase letters

letters = []
while True:
    l = input("Enter a character (Press end to stop) : ")
    if l == "end":
        break
    letters.append(l)


for m in filter(lambda n : str.isupper(n),letters):
    print(m)
