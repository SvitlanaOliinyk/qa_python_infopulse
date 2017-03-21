import datetime


class Emp:
    def __init__(self, name_surname, start_work=None, salary=0):
        self.name_surname = name_surname
        self.start_work = start_work
        self.salary = salary

    def name(self):
        """
        Функция, определяющая имя сотрудника
        """
        return self.name_surname.split(' ')[0]

    def surname(self):
        """
        Функция, определяющая фамилию сотрудника
        """
        return self.name_surname.split(' ')[1]

    def month_salary(self, number_of_month):
        """
        Функция, определяющая доход сотрудника за введенное количество месяцев
        """
        return int(number_of_month) * float(self.salary)

    def position(self, expi):
        """
        Функция, определяющая опыт работы сотрудника и его квалификацию
        """
        a = expi.split('-')
        experience = int(str(datetime.date.today() - datetime.date(int(a[0]),int(a[1]),int(a[2]))).split()[0]) / 365
        if experience < 3:
            return 'Junior'
        elif 3 < experience < 6:
            return 'Middle'
        elif experience > 6:
            return 'Senior'
