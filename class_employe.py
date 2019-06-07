# create a class to accept employe details
class Employe:
    def __init__(self, roll, name, designation="None", salary=0):
        self.roll = roll
        self.name = name
        self.designation = designation
        self.salary = salary

    def change_designation(self, newdes):
        self.designation = newdes

    def change_salary(self, newsal):
        self.salary = newsal

    @property
    def net_salary(self):
        hra = 0.3 * self.salary
        pf = 0.02 * self.salary
        a = self.salary
        a += hra
        a -= pf
        return a

    def __str__(self):
        return f"{self.roll} - {self.name} - {self.designation} - {self.salary}"

    def __eq__(self, other):
        return self.roll == other.roll

    def __gt__(self, other):
        return self.salary > other.salary

    @property
    def bonus(self):
        if self.salary >= 15000:
            return 0.4 * self.salary
        else:
            return 0.5 * self.salary


class Programmer(Employe):
    def __init__(self, roll, name, salary, language):
        super().__init__(roll, name, salary)
        self.language = language

    def get_salary(self):
        return self.get_salary()


class Administator(Employe):
    def __init__(self, roll, name, database, hours, hours_rate):
        super().__init__(roll, name)
        self.database = database
        self.hours = hours
        self.hours_rate = hours_rate

    def get_salary(self):
        if __name__ == '__main__':
            return self.hours * self.hours_rate


if __name__ == "__main__":
    a1 = Employe(123, "lokesh", "general manager", 100)
    a2 = Administator(987654, "Manmadha rao", "oracle", 98, 1000)
    print(str(a1))
    print(str(a2))
    print(a1 > a2)
    print(a1 < a2)
    print(a1 == a2)
    print(a1 != a2)
    a1.change_designation("CEO")
    a1.change_salary(100)
    a1.net_salary
    print(a1.designation)
    print(a1.salary)
    print(a1.net_salary)
    print(a1.salary)
    print(a1.bonus)
    print(a2.get_salary())
