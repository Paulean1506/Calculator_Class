class Calculator:
    def __init__(self):
        self.operations = ['1', '2', '3', '4']

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2