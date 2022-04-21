class Carcass:
    __some_car_details = True


class WheelsBase:
    __blocked = True

    def unblock_wheels(self):
        print('wheels unblocked')
        self.__blocked = False


class Motor:

    __motor = False

    def turn_on_motor(self):
        print('Motor turned on')
        self.__motor = True


class Car(Carcass, WheelsBase, Motor):

    def drive(self):
        self.turn_on_motor()
        self.unblock_wheels()
        print('the vehicle starts moving\n')

    def make_sound(self):
        pass


class PoliceCar(Car):

    def make_sound(self):
        print('Caution! The police is driving\n')


class AmbulanceCar(Car):

    def make_sound(self):
        print('Caution! The ambulance is driving\n')


if __name__ == '__main__':
    car = Car()
    car.drive()

    police = PoliceCar()
    police.drive()
    police.make_sound()

    ambulance = AmbulanceCar()
    ambulance.drive()
    ambulance.make_sound()
