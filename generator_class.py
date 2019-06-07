# create a iterator using generator that returns capital letters
def upper_letters():
    for i in range(65,91):
        yield chr(i)
for ch in upper_letters():
    print(ch)
