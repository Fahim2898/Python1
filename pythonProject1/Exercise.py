from Class_OOP import Student


class Triangle:
    base = ''
    height = ''

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print('Area=', area)


class nothing (Student):
    print('Nothing Class')


t1 = Triangle(10, 20)
t1.calculate_area()


t2 = Triangle(20, 30)
t2.calculate_area()

tt1 = nothing(1009,'Shakib Sha', 3.99)

x = 1 + 2 * 3 - 8 / 4
print(x)