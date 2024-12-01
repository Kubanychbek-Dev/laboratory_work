class Shape:
    def __init__(self, length):
        self.length = length


class Square(Shape):
    def get_length(self):
        return f"Сторона квадрата равен {self.length}"

    def get_circle_r(self):
        return (f"Если сторона квадрата равна {self.length}, то радиус "
                f"окружности, вписанной в этот квадрат будет равен {int(self.length / 2)}")


class Circle(Shape):
    def get_length(self):
        return f"Радиус окружности равнa {self.length}"

    def get_square_a(self):
        square_length = (self.length * 2) ** 2
        return (f"Если радиус окружности равен {self.length}, то сторона "
                f"квадрата будет равен {self.length * 2}"
                f"\nПлощадь квадрата будет равен {square_length}")


square = Square(46)
print(square.get_length())
print(square.get_circle_r())
print()

circle = Circle(23)
print(circle.get_length())
print(circle.get_square_a())