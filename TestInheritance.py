from User_Interface import UserInterface
from Inheritance import InheritCalculator

Inp = UserInterface()
InCal = InheritCalculator()


num1 = Inp.ask_user_input()
num2 = Inp.ask_user_input()

sum = InheritCalculator.addition(self= InheritCalculator, num1= num1, num2= num2)
print("\n\033[92mThe sum of", num1, "and", num2, "is:", sum)

diffence = InheritCalculator.subtraction(self= InheritCalculator, num1= num1, num2= num2)
print("\n\033[93mThe difference of", num1, "and", num2, "is:", diffence)

product = InheritCalculator.multiplication(self= InheritCalculator, num1= num1, num2= num2)
print("\n\033[94mThe product of", num1, "and", num2, "is:", product)

quotient = InheritCalculator.division(self= InheritCalculator, num1= num1, num2= num2)
print("\n\033[95mThe quotient of", num1, "and", num2, "is:", quotient)

power = InheritCalculator.power(self= InheritCalculator, num1= num1, num2= num2)
print("\n\033[91mThe first number,", num1, "raised to the power of", num2, "is:", power)

sr = InheritCalculator.square_root(self= InheritCalculator, num1= num1)
print("\n\033[96mThe Square root of",num1, "is:", sr)

