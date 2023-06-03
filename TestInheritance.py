from User_Interface import UserInterface
from Class_Calculator import Calculator
from Inheritance import InheritCalculator
from IPython.display import display

Inp = UserInterface()
calculate = Calculator()
InCal = InheritCalculator()


num1 = Inp.ask_user_input()
num2 = Inp.ask_user_input()

sum = InheritCalculator.addition(self= InheritCalculator, num1= num1, num2= num2)
display("The sum is:" + sum)