# to verify the mro for hirachy
class A:
    def process(self):
        print("In A ")


class B(A):
    def process(self):
        print("In B")


class C(A,B):
    def process(self):
        print("Inn C")


print(C.mro())
