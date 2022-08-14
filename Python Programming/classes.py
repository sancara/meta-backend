from curses.ascii import EM
from unicodedata import name


class Employee:
    def __init__(self, name, last ) -> None:
        self.name = name
        self.last = last

class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employee):
    def leave_request(self, days):
        return f'May I take a leave for {days} days'

adrian = Supervisor('Adrian', 'A', "apple")

emily = Chefs('Emily', 'E')
adrian = Chefs('Adrian', 'A')

print(emily.leave_request(14))