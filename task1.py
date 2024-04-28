class Trapezoid:

    def __init__(self, base_a, base_b, side_c, side_d, h):
        self.base_a = base_a
        self.base_b = base_b
        self.side_c = side_c
        self.side_d = side_d
        self.h = h

    def get_square(self):
        return ((self.base_b+self.base_a)/2)*self.h

    def get_perimetr(self):
        return self.base_a + self.base_b + self.side_c + self.side_d


trapezia = Trapezoid(10, 5, 4, 4, 2)  # все стороны указаны в метрах
print(f"Площадь трапеции: {Trapezoid.get_square(trapezia)} м^2")
print(f"Периметр трапеции: {Trapezoid.get_perimetr(trapezia)} м")
