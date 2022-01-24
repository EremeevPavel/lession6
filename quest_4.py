from random import choice


class Car:
    direction = ['North', 'South', 'West', 'East']


    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f'Новая машина: {name}, расцветки {color}.\n Это полиция? {police}')


    def go(self):
        print(f'{self.name}: Поехали!')

    def stop(self):
        print(f'{self.name}: Остановись!')

    def turn(self):
        print(f'{self.name}: Куда едем?!{choice(self.direction)}')

    def speed_foo(self):
        print(f'{self.name}: Скорость: {self.speed}')


class TownCar(Car):
    def speed_foo(self):
        return f'Авто: {self.name} Скорость: {self.speed}. Осторожно!: ' if self.speed > 60 else super().speed_foo()


class WorkCar(Car):
    def speed_foo(self):
        return f'Авто: {self.name} Скорость: {self.speed}. Осторожно!: ' if self.speed > 40 else super().speed_foo()

class PolceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, police=True)


police_car = PolceCar('Полиция', 'По форме', 100)
town_car = TownCar('Грузовик', 'Серый', 45)
work_car = WorkCar('Седан', 'Белый', 65)

list_car = [police_car, town_car, work_car]

for el in list_car:
    el.go()
    print(el.speed_foo())
    el.turn()
    el.stop()
    print()
