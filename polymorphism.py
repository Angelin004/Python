class animal():
    def sound(self):
        print("animal makes sound")

class dog():
    def sound(self):
        print("dog barks")

a1=animal()
a1.sound()

a2=dog()
a2.sound()

#method overriding
class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")

b1=dog()
a1.sound()

#eg
class bird():
    def sound(self):
        print("birds are beautiful")

class animal(bird):
    def sound(self):
        print("animal makes sound")

c1=bird()
c1.sound()