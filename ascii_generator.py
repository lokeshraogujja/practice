# create a generator called code that accpts strings and returns ascii codes
def codes(s):
    for i in range(0, len(s)):
        yield s[i]


l = input("Enter a string : ")
for n in codes(l):
    print(f"The ASCII code of {n} is : {ord(n)}")
