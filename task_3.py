class Pets:
    def __init__(self, name, typeof):
        self.__name = name
        self.__typeof = typeof

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__typeof


class Dog(Pets):
    def __init__(self, name, typeof, sound):
        super().__init__(name, typeof)
        self.__sound = sound

    def get_sound(self):
        return self.__sound


class Cat(Pets):
    def __init__(self, name, typeof, sound):
        super().__init__(name, typeof)
        self.__sound = sound

    def get_sound(self):
        return self.__sound


dog = Dog("Reks", "немецкая овчарка", "Гав")
print(f"Имя: {dog.get_name()}")
print(f"Вид: {dog.get_type()}")
print(f"Звук: {dog.get_sound()}")
print()

cat = Cat("Гарфилд", "Персидский кот", "Мяу")
print(f"Имя: {cat.get_name()}")
print(f"Вид: {cat.get_type()}")
print(f"Звук: {cat.get_sound()}")
