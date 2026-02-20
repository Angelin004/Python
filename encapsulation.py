class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print(self.__name, self.__marks)

s1 = Student("Angel", 90)
s1.display()