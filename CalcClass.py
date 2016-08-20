class Calculator:
    def __init__(self):
        print('Simple Python Addition Calculator Program')
        print(' ')
        print(' ')

    def addNumbers(self, int1, int2):
        answer = int1 + int2
        print(' ')
        print('The sum of both numbers is:  ' , answer)

    def subNumbers(self, int1, int2):
        answer = int1 - int2
        print(' ')
        print('The difference of both numbers is:  ' , answer)

    def multiNumbers(self, int1, int2):
        answer = int1 * int2
        print(' ')
        print('The product of both numbers is:  ' , answer)

    def divideNumbers(self, int1, int2):
        answer = int1 / int2
        print(' ')
        print('The quotient of both numbers is:  ' , int(answer))
