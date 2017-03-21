import datetime


class Emp:
    def __init__(self, name_surname, start_work=None, salary=0):
        self.name_surname = name_surname
        self.start_work = start_work
        self.skills = []
        self.salary = salary

    def name(self):
        """
        Функция, определяющая имя сотрудника
        """
        try:
            print('Имя сотрудника ', self.name_surname.split(' ')[0])
        except IndexError:
            print('Некорректный ввод')

    def surname(self):
        """
        Функция, определяющая фамилию сотрудника
        """
        try:
            print('Фамилия сотрудника ', self.name_surname.split(' ')[1])
        except IndexError:
            print('Введено только имя')

    def month_salary(self, number_of_month):
        """
        Функция, определяющая доход сотрудника за введенное количество месяцев
        """
        try:
            print('Зарплата за введенное количество месяцев составляет ', (int(number_of_month) * float(self.salary)))
        except (SyntaxError, ValueError, TypeError):
            print('Ошибка ввода количества месяцев')

    def position(self, expi):
        """
        Функция, определяющая опыт работы сотрудника и его квалификацию
        """
        try:
            a = expi.split('.')
            experience = int(str(datetime.date.today() - datetime.date(int(a[0]),int(a[1]),int(a[2]))).split()[0]) / 365
            if experience < 3:
                print('Сотрудник занимает позицию Junior')
            elif 3 < experience < 6:
                print('Сотрудник занимает позицию Middle')
            elif experience > 6:
                print('Сотрудник занимает позицию Senior')
        except (SyntaxError, ValueError, TypeError):
            print('Ошибка ввода даты. Неверный формат ввода.')
