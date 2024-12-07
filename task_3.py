class Pets:
    def __init__(self, name, typeof):
        self.__name = name
        self.__typeof = typeof

    def __str__(self):
        return f"Имя: {self.__name}\nВид: {self.__typeof}"


class Dog(Pets):
    def __init__(self, name, typeof, sound):
        super().__init__(name, typeof)
        self.__sound = sound

    def __str__(self):
        return f"{super().__str__()}\nЗвук: {self.__sound}"


class Cat(Pets):
    def __init__(self, name, typeof, sound):
        super().__init__(name, typeof)
        self.__sound = sound

    def __str__(self):
        return f"{super().__str__()}\nЗвук: {self.__sound}"


dog = Dog("Reks", "немецкая овчарка", "Гав")
print(dog)
print()

cat = Cat("Гарфилд", "Персидский кот", "Мяу")
print(cat)