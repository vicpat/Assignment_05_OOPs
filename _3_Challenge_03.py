#  Challenge 3: 
#  Implement the Complete Student Class

class Student:

    def setName(self, name):
        self.name = name
        return

    def getName(self):
        self.name
        return

    def setRollNumber(self, RollNumber):
        self.RollNumber = RollNumber
        return

    def getRollNumber(self):
        return

    def display(self):
      print("Student's name is", self.name,'and Roll number is', self.RollNumber)

obj = Student()
obj.setName("Vaibhavi")
obj.setRollNumber('21')
obj.display()