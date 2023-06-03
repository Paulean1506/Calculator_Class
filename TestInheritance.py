from User_Interface import UserInterface
from Inheritance import InheritCalculator
from termcolor import colored
from pyfiglet import Figlet

Inp = UserInterface()
InCal = InheritCalculator()

while True:
    num1 = Inp.ask_user_input()
    num2 = Inp.ask_user_input()

    sum = InCal.addition(num1= num1, num2= num2)
    print("\n\033[92mThe sum of", num1, "and", num2, "is:", sum)

    diffence = InCal.subtraction(num1= num1, num2= num2)
    print("\n\033[93mThe difference of", num1, "and", num2, "is:", diffence)

    product = InCal.multiplication(num1= num1, num2= num2)
    print("\n\033[94mThe product of", num1, "and", num2, "is:", product)

    quotient = InCal.division(num1= num1, num2= num2)
    print("\n\033[95mThe quotient of", num1, "and", num2, "is:", quotient)

    power = InCal.power(num1= num1, num2= num2)
    print("\n\033[91mThe first number,", num1, "raised to the power of", num2, "is:", power)

    sr = InCal.square_root(num1= num1)
    print("\n\033[96mThe Square root of",num1, "is:", sr)

    sr = InCal.square_root(num1= num2)
    print("\n\033[97mThe Square root of",num2, "is:", sr)

    try_again = input("\nDo you want to try again? 'y' or 'n': ")
    if try_again.lower() == "n":
        r = Figlet(font = "cybermedium")
        print(colored(r.renderText('\nThank you!'), 'red'))
        break
        

