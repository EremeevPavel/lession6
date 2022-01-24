class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'ФИО: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Общая сумма дохода: {sum(self._income.values())}'


a = int(input('Введи оклад: '))
b = int(input('Введи бонус: '))
manager = Position('Ivan', 'Ivanov', 'manager', a, b)
print(manager.get_full_name())
print(f'Должность:', manager.position)
print(manager.get_total_income())
