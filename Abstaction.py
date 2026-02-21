class featureplan(ABC):
    def login(self):
        pass
    def logout(self):
        pass
    def checkout(self):
        pass

#developer implement it
class webapp(featureplan):
    def login(self):
        print("webapp login done")
    def logout(self):
        print("webapp logout done")

app=webapp()
app.login()
app.logout()

#eg
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of square")


