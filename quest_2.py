class Road:

    def __init__(self, length, width):
        self._lenght = length
        self._widht = width

    def fool_prof(self, weight=25, thickness=5):
        return f'{self._lenght} m * {self._widht} m * {weight} kg * {thickness} cm = ' \
               f'{(self._lenght * self._widht * weight * thickness) / 1000} t'


road_int = Road(5000, 20)
print(road_int.fool_prof())
