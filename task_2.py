class Engine:
    def __init__(self, horse_power):
        self.__horse_power = horse_power

    def get_power(self):
        return self.__horse_power


class Wheel:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size


class Door:
    def __init__(self, amount):
        self.__amount = amount

    def get__door(self):
        return self.__amount


class Car:
    def __init__(self, make, model, horse_power, wheel_size, door_amount):
        self.__make = make
        self.__model = model
        self.__horse_power = Engine(horse_power)
        self.__wheel_size = Wheel(wheel_size)
        self.__door_amount = Door(door_amount)

    def get_car(self):
        return (f"{self.__make} {self.__model}. Мощность двигателя: {self.__horse_power.get_power()} л/с."
                f" Размер колес: {self.__wheel_size.get_size()}. Количество дверей: {self.__door_amount.get__door()}.")


car1 = Car("Shevrolet", "Tahoe", 420, 22, 5)
print(car1.get_car())
print()

car2 = Car("Porsche", 918, 608, 20, 2)
print(car2.get_car())