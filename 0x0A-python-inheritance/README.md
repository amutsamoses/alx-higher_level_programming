0x0A. Python - Inheritance
Python
OOP
Inheritance

Inheritance in object-oriented programming is inspired by the real-world inheritance in human beings. We acquire some of the traits of our parents during birth.

In Python, inheritance is the capability of a class to pass some of its properties or methods to it’s derived class(child class). With inheritance, we build a relationship between classes based on how they are derived.
To derive a class from another class we can simply use the name of the parent class in parentheses after the class name.

Code:

class Fruit:
  pass

class Apple(Fruit):
  pass

The pass statement is used to create an empty class. Python has an in-built function issubclass() to check if a class is a subclass of another or not.
Code:

issubclass(Apple, Fruit)

1. Single Inheritance in Python
In single inheritance, a single class inherits from a class. This is the simplest form of inheritance.single inheritance in python

Code:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def display(self):
        print("Child method")


c = Child()
c.display()
c.show()

2. Multilevel Inheritance in Python
Python supports multilevel inheritance, which means that there is no limit on the number of levels that you can inherit. We can achieve multilevel inheritance by inheriting one class from another which then is inherited from another class.multilevel inheritance in python

Code:

class A:
    def methodA(self):
        print("A class")

class B(A):
    def methodB(self):
        print("B class")

class C(B):
    def methodC(self):
        print("C class")

c = C()
c.methodA()
c.methodB()
c.methodC()

3. Multiple Inheritance in Python
Till now, we were inheriting from only one class at a time.

In multiple inheritance, we will see that Python also allows us to inherit from more than one class. To achieve this we can provide multiple classes separated by commas.multiple python inheritance

Code:

class A:
    def methodA(self):
        print("A class")

class B:
    def methodB(self):
        print("B class")

class C:
    def methodC(self):
        print("C class")

class D(A, B, C):
    def methodD(self):
        print("D class")

d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()

4. Hierarchical Inheritance in Python
In a hierarchical inheritance, a class is inherited by more than one class. It is simple to understand with a diagram.hierarchical python inheritance

Code:

class A:
    def methodA(self):
        print("A class")

class B(A):
    def methodB(self):
        print("B class")

class C(A):
    def methodC(self):
        print("C class")

b = B()
c = C()

b.methodA()
c.methodA()

5. Hybrid Inheritance in Python
The term Hybrid describes that it is a mixture of more than one type. Hybrid inheritance is a combination of different types of inheritance.hybrid python inheritance

Code:

class A:
    def methodA(self):
        print("A class")

class B(A):
    def methodB(self):
        print("B class")

class C(A):
    def methodC(self):
        print("C class")

class D(B,C):
    def methodD(self):
        print("D class")

d = D()
d.methodA()
