class Employer:
    def __init__(self, firstname, lastname, age):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age

    def __str__(self):
        return f"имя: {self.__firstname}\nфамилия: {self.__lastname}\nвозраст: {self.__age}"


class President(Employer):
    def __init__(self, firstname, lastname, age, position):
        super().__init__(firstname, lastname, age)
        self.__position = position

    def get_position(self):
        print(f"должность: {self.__position}")


president = President("Садыр", "Жапаров", 50,
                      "Президент Кыргызской Республики")
print(president)
president.get_position()
print()

class Manager(Employer):
    def __init__(self, firstname, lastname, age, position):
        super().__init__(firstname, lastname, age)
        self.__position = position

    def get_position(self):
        print(f"должность: {self.__position}")


manager = Manager("Ти́моти (Тим)", "До́нальд Кук", 64,
                  "Генеральный директор компании Apple")
print(manager)
manager.get_position()
print()


class Worker(Employer):
    def __init__(self, firstname, lastname, age, position):
        super().__init__(firstname, lastname, age)
        self.__position = position

    def get_position(self):
        print(f"должность: {self.__position}")

worker = Worker("John", "Doe", 34, "Строитель")
print(worker)
worker.get_position()