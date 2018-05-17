import re
from abc import ABCMeta, abstractmethod


class Rule(metaclass=ABCMeta):

    @abstractmethod
    def change_rule(self, new_re):
        pass


class IDRule(Rule):
    def __init__(self):
        self.empid = "^[A-Z][\d]{3}$"

    def change_rule(self, new_re):
        self.empid = '"' + new_re + '"'


class GenderRule(Rule):
    def __init__(self):
        self.gender = "^(M|F)$"

    def change_rule(self, new_re):
        self.gender = '"' + new_re + '"'


class AgeRule(Rule):
    def __init__(self):
        self.age = "^[\d]{2}$"

    def change_rule(self, new_re):
        self.age = '"' + new_re + '"'


class SalesRule(Rule):
    def __init__(self):
        self.sales = "^[\d]{3}$"

    def change_rule(self, new_re):
        self.sales = '"' + new_re + '"'


class BMIRule(Rule):
    def __init__(self):
        self.bmi = "^((n|N)ormal)|((o|O)verweight)|((o|O)besity)|((u|U)nderweight)$"

    def change_rule(self, new_re):
        self.bmi = '"' + new_re + '"'


class SalaryRule(Rule):
    def __init__(self):
        self.salary = "^([\d]{2}|[\d]{3})$"

    def change_rule(self, new_re):
        self.salary = '"' + new_re + '"'


class BirthdayRule(Rule):
    def __init__(self):
        self.birthday = "^(((0[1-9])|([1-31]))|[1-2][0-9]|3(0|1))(/)(((0[1-9])|([1-12]))|1[0-2])(/)(19|20)[0-9]{2}$"

    def change_rule(self, new_re):
        self.birthday = '"' + new_re + '"'
