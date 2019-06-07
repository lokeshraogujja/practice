# create a class that return capital letters using a iterator
class Upper_case_iterartor:
    def __init__(self):
        self.start = "A"

    def __next__(self):
        if ord(self.start) > 90:
            raise StopIteration
        else:
            self.start = chr(ord(self.start) + 1)
            return chr(ord(self.start)-1)
class upper_case:
    def __iter__(self):
        return Upper_case_iterartor()

for n in upper_case():
    print(n)