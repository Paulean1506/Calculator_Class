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

        # Ask the name of the user
        name=input("\nWhat's your name? ")
        print("\n")
        print("         \\|||||/        ")
        print("         ( OᴗO )         ")
        print("+--ooO------------------+")
        print("|                       |")
        print("|     Hello " + name + "     |")
        print("|                       |")
        print("+------------------Ooo--+")
        print("         |__||__|        ")
        print("          ||  ||         ")
        print("         ooO  Ooo        ")

        # Use a while loop to continuously prompt the user for an operation
        while True:

            # Ask the user to choose one of the four math operations
            table = PrettyTable()
            table.title = '\033[95mSelect operation:'
            table.field_names = ['Operation', 'Choice']
            table.align['Operation'] = 'l'
            table.add_row(['a.) Addition', 1])
            table.add_row(['b.) Subtraction', 2])
            table.add_row(['c.) Multiplication', 3])
            table.add_row(['d.) Division', 4])
            print(table)
            
            try:
                operation = input("\n\033[92mPlease enter your chosen operation (1/2/3/4): ")

                # Raise Exception
                if operation not in self.operations:
                    raise ValueError
            
                # Ask user for two integers
                num1 = int(input("Enter the first integer: "))
                num2 = int(input("Enter the second integer: "))

                # Perform addition and display result
                if operation == '1':
                    result = self.addition(num1, num2)
                    print("\n\033[93mThe result of", num1, "+", num2, "is:", result)

                # Perform subtraction and display result
                elif operation == '2':
                    result = self.subtraction(num1, num2)
                    print("\n\033[93mThe result of", num1, "-", num2, "is:", result)

                # Perform multiplication and display result
                elif operation == '3':
                    result = self.multiplication(num1, num2)
                    print("\n\033[93mThe result of", num1, "*", num2, "is:", result)

                # Perform division and display result
                elif operation == '4':
                    result = self.division(num1, num2)
                    print("\n\033[93mThe result of", num1, "/", num2, "is:", result)

            # Apply the appropriate exceptions
            except ValueError:
                print("\n\033[31mSorry! Invalid input, please enter one of the given choices")
            except ZeroDivisionError:
                print("\n\033[31mSorry! You are dividing by zero")

            # Ask if the user wants to try again or not
            choice = input("\n\033[96mDo you want to try again? 'y' or 'n': ")

            # Raise Value error
            if choice not in ["y", "n"]:
               raise ValueError

            # If yes, repeat Step 1
            if choice == 'y':
                continue

            # If no, Display “Thank you!” and the program will exit
            else:
                r = Figlet(font = "cybermedium")
                print(colored(r.renderText('\nThank you!'), 'red'))
                break
