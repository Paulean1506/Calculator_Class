from Class_Calculator import Calculator

class InheritCalculator(Calculator):
    def power(self, num1, num2):
        return num1 ** num2
    
    def square_root(self, num1):
        return num1 ** 0.5