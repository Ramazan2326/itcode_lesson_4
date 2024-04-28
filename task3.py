class Calculator:

    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def summator(self):
        return self.num_a + self.num_b

    def substraction(self):
        return self.num_a - self.num_b

    def multiplication(self):
        return self.num_a * self.num_b

    def divide(self):
        return int(self.num_a/self.num_b)


a = int(input("Введите число: "))
b = int(input("Введите второе число: "))
print(f"Результат сложения числа a на число b: {Calculator(a, b).summator()}")
print(f"Результат вычитания из числа a число b: {Calculator(a, b).substraction()}")
print(f"Результат умножения числа a на число b: {Calculator(a, b).multiplication()}")
print(f"Результат деления числа a на число b: {Calculator(a, b).divide()}")
