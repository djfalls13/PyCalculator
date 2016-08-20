### Clear the screen

import os
os.system('cls' if os.name == 'nt' else 'clear')

from CalcClass import Calculator

x = Calculator()

print(' 1 for Addition')
print(' 2 for Subtraction')
print(' 3 for Multiplication')
print(' 4 for Division')

mode = input('Enter Calculation Type: ')
mode = int(mode)
print(' ')

while mode < 1 or mode > 4:
    if mode < 1 or mode > 4:
        print('Only enter a number between 1 and 4')
        mode = input('Enter Calculation Type: ')
        mode = int(mode)
    else:
        pass

num1 = input('Enter first number: ')
print(' ')
num2 = input('Enter second number: ')

if mode == 1:
    x.addNumbers(int(num1), int(num2))

elif mode == 2:
    x.subNumbers(int(num1), int(num2))

elif mode == 3:
    x.multiNumbers(int(num1), int(num2))

elif mode == 4:
    x.divideNumbers(int(num1), int(num2))

else:
    print('Error')
