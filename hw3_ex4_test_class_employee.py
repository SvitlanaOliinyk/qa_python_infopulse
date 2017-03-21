# import datetime
# from hw3_ex1_class_employee import Emp

# k = Emp(name_surname='Vate Loda', salary=2)

# k.name()        # Функция, определяющая имя сотрудника
# k.surname()         # Функция, определяющая фамилию сотрудника

# num_month = input('Введите количество месяцев, за которые рассчитать зарплату ')
# k.month_salary(num_month)         # Функция, определяющая доход сотрудника за введенное количество месяцев

# start_work = input('Введите дату приема на работу в формате ГГГГ.ММ.ДД ')
# k.position(start_work)           # Функция, определяющая опыт работы сотрудника и его квалификацию

import datetime
import unittest
from hw3_ex1_class_employee import Emp


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Emp('Svet Oliin', salary=10)

    def test_name(self):
        self.assertEqual(self.emp.name(), 'Svet')

    def test_surname(self):
        self.assertEqual(self.emp.surname(), 'Oliin')

    def test_month_salary(self):
        self.assertEqual(self.emp.month_salary(6), 60)

    def test_position_jun(self):
        self.assertEqual(self.emp.position('2016-01-01'), 'Junior')

    def test_position_mid(self):
        self.assertEqual(self.emp.position('2013-01-01'), 'Middle')

    def test_position_sin(self):
        self.assertEqual(self.emp.position('2010-01-01'), 'Senior')

if __name__ == "__main__":
    unittest.main()
