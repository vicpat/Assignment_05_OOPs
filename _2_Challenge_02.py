#  Challenge 2:
#  Implement a Calculator Class.

class Calculator:

    def __init__(self):
      self.num1 = 10
      self.num2 = 94
      print('the given number is 10 and 94')

    def add(self):
      a = self.num1 + self.num2
      print('addition is --', a)

    def subtract(self):
      b = self.num1 - self.num2
      print('subtract is --', b)

    def multiply(self):
      c = self.num1 * self.num2
      print('multiply is --', c)

    def divide(self):
      d = self.num2 / self.num1
      print('divide is --', d)


obj = Calculator()
obj.add()
obj.subtract()
obj.multiply()
obj.divide()