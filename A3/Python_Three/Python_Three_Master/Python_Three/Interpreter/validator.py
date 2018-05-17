import re
from copy import deepcopy
from rule import *


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.empid = IDRule()
        self.gender = GenderRule()
        self.age = AgeRule()
        self.sales = SalesRule()
        self.bmi = BMIRule()
        self.salary = SalaryRule()
        self.birthday = BirthdayRule()

    def check_all(self, new_value, new_key):
        """
        :param new_value:
        :param new_key:
        :return:
        """
        key_1 = new_key.lower()
        key_2 = getattr(self, key_1)
        key_3 = getattr(key_2, key_1)
        check_value = str(new_value)
        check_value = self.fix_bday_delims(check_value)
        check_value = self.fix_gender(check_value)
        match = re.match(key_3, check_value)
        if match:
            asd = check_value
            return asd
        elif match is None:
            return False

    @staticmethod
    def fix_gender(new_gender):
            match = re.match("^(m|M)ale$", new_gender)
            fmatch = re.match("^(f|F)emale$", new_gender)
            if match:
                new_gender = "M"
            elif fmatch:
                new_gender = "F"
            return new_gender

    @staticmethod
    def fix_bday_delims(new_birthday):
        invalid_delims = "^(|/\\.:;,_-)$"
        for i in invalid_delims:
            new_birthday = new_birthday.replace(i, "/")
        return new_birthday

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

    def checker(self, row):
        for key, value in row.items():
            valid_keys = {"id", "empid", "gender", "age", "sales", "salary", "birthday", "bmi"}
            key2 = key.lower()
            if key2 in valid_keys:
                if key2 == "id":
                    key2 = "empid"
                elif key2 == "bmi":
                    value = value.lower()
                else:
                    key2 = key2.lower()
                if self.check_all(value, key2) is False:
                    return False
                else:
                    self.push_value(key2.capitalize(), self.check_all(value, key2))
            else:
                return False

    def save_dict(self, loaded_dict):
        for empno, row in loaded_dict.items():
            b = self.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                self.push_row(empno)
        return self.return_dict()

    def push_value(self, key, val):
        self.temp_dict[key] = val

    def push_row(self, empno):
        print("Adding Row " + str(empno))
        temp = deepcopy(self.temp_dict)
        self.valid_dict[empno] = temp
        print(self.valid_dict[empno])

    def return_dict(self):
        return self.valid_dict


# a = Validator()
# dictionary = {'ID': 'Q999', 'Gender': 'F', 'Age': '21',
#               'Sales': '001', 'BMI': 'Normal', 'Salary': '12', 'Birthday': '01/01/1996'}
#
# a.checker(dictionary)
# print(a.temp_dict)

# key_1 = new_key.lower()
# key_2 = getattr(self, key_1)
# key_3 = key_2.rule
# check_value = str(new_value)
# check_value = self.fix_bday_delims(check_value)
# check_value = self.fix_gender(check_value)
# match = re.match(key_3, check_value)

