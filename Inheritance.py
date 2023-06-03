from Class_Calculator import Calculator
from User_Interface import UserInterface

class InheritCalculator(Calculator):
    def power(self, num1, num2):
        return num1 ** num2
    
    def square_root(self, num1):
        return num1 ** 0.5
    
class InheritUI(UserInterface):
    def try_again(self):
        while True:
            TA = input("\n\033[96mDo you want to try again? 'y' or 'n': ")
            if TA in ["y", "n"]:

                if TA == 'y':
                    continue

            else:
                print('\nThank you!')
                break
