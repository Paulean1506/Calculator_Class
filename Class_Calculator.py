# Paulean Marguerette F. Parrish
# BSCPE 1-4
# Converted Calculator

# Class for the four basic operations
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
        
    # Function used to run the calculator
    def run_calculator(self):

        from termcolor import colored
        from pyfiglet import Figlet
        from prettytable import PrettyTable

        print('=' * 54)
        f = Figlet(font = "standard")
        print(colored(f.renderText('Oh, Hi there!'), 'cyan'))
        print('=' * 54)

        