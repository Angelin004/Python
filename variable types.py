#instance
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Angel", 20)
s2 = Student("John", 21)

print(s1.name)
print(s2.name)

#class
class Student:
    college = "ABC College"   # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Angel")
s2 = Student("John")

print(s1.college)
print(s2.college)

#local
class Demo:
    def show(self):
        x = 10   # local variable
        print(x)

obj = Demo()
obj.show()
