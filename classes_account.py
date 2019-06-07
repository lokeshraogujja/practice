# craeting a class to have account number coustmer name and balance
class Account:
    def __init__(self, accno, cosname, bal=0):
        self.accno = accno
        self.cosname = cosname
        self.bal = bal

    def deposite(self, amt):
        self.bal += amt

    def withdrawel(self, mon):
        if mon < self.bal:
            self.bal -= mon
        else:
            print("Insufficiant Funds")

    def get_balance(self):
        return self.bal


a1 = Account(234556, "lokesh", 10000)
a2 = Account(1234567,"manmadha rao",1000000000)

a1.withdrawel(2000)
a2.deposite(123456)

print(a1.bal)
print(a2.bal)