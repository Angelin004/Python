#try and except
try:
    a = int(input("Enter number: "))
    print(10 / a)
except:
    print("Error occurred")

#handling specific exceptions
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


try:
    a=int(input())
    b=int(input())
    print(a+b)
except Exception as e:
    print("something",e)

#value error
try:
    a=int()
    b=int()
    print(a+b)
except value error as e:
    print("value error",e)

#type error
try:
    a=int(input())
    b=int(input())
    c=int()
    print(c/a)
except type error as e:
    print("type error",e)

#name error
try:
    a=int(input())
    b=int(input())
    c=int()
    print(c/a)
    print("d")
except type error as e:
    print("type error",e)

#compile time error
printt("hi")

#logical error
a=10
b=10
print(a+a)

#runtime error
a=int(input())
b=int(input())
print(a+b)

#finally
try:
    a=int(input())
    b=int(input())
    c=int()
    print("d")
except type error as e:
    print("type error",e)
except exception:
    print("something wrong")
finally:
    print("done")

#raise
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")




