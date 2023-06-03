from User_Interface import UserInterface
from Class_Calculator import Calculator
from Inheritance import InheritCalculator

Inp = UserInterface()
calculate = Calculator()
InCal = InheritCalculator()


num1 = Inp.ask_user_input()
num2 = Inp.ask_user_input()

sum = InheritCalculator.addition(self= InheritCalculator, num1= num1, num2= num2)
print("\033[92mSum:",sum)

diffence = InheritCalculator.subtraction(self= InheritCalculator, num1= num1, num2= num2)
print("\033[93mDiffence:",diffence)

product = InheritCalculator.multiplication(self= InheritCalculator, num1= num1, num2= num2)
print("\033[94mProduct:",product)

quotient = InheritCalculator.division(self= InheritCalculator, num1= num1, num2= num2)
print("\033[95mQuotient:",quotient)