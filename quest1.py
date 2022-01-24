from time import sleep


class TrafficLight:
    _color = 'Black'

    def running(self):
        while True:
            print('Traffic light is red')
            sleep(7)
            print('Traffic light is yellow')
            sleep(2)
            print('Traffic light is green')
            sleep(7)


tl = TrafficLight()
tl.running()
