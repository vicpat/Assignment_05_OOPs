#  Challenge 1: 
#  Square Numbers and Return Their Sum.

class point:

    def __init__(self):

        self.x=1
        self.y=3
        self.z=5

    def sqSum(self):
      self.x = self.x ** 2
      self.y = self.y ** 2
      self.z = self.z ** 2
      print("sqsum is --", (self.x, self.y, self.z))

    def sum(self):
      print("sum is:", self.x + self.y + self.z)

obj = point()
obj.sqSum()
obj.sum()