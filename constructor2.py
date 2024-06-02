class Student:
    def __init__(self, name, rollNum, javaMarks, pythonMarks, mathsMarks):
        self.name = name
        self.rollNum = rollNum
        self.javaMarks = javaMarks 
        self.pythonMarks = pythonMarks 
        self.mathsMarks = mathsMarks
 
    def printAllDetails(self):
        print(self.name)
        print(self.rollNum)
        print(self.javaMarks)
        print(self.pythonMarks)
        print(self.mathsMarks)
 
obj = Student("Kumar", 501, 67, 45, 78)
obj.printAllDetails()
 
obj2 = Student("Kumar1", 501, 67, 45, 78)
obj2.printAllDetails()
 
# obj2 = Student()
# print(obj2.name)
# print(obj2.rollNum)
# print(obj2.javaMarks)