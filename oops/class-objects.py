# class → Blueprint.
# object → Instance of a class.
# __init__() → Constructor-like initializer.
# self → Reference to the current object.
# self.brand → Instance variable.
# drive() → Instance method.

class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("BMW")
print(car1.brand)

# In this example, we define a class `Car` with an `__init__` method that initializes the `brand` attribute. 
# We then create an instance of the `Car` class called `car1` and print its `brand`.

# Java
# class Car {
#     String brand;

#     Car(String brand) {
#         this.brand = brand;
#     }
# }

# Car car1 = new Car("BMW");
# System.out.println(car1.brand);


# Important differences
# Concept	            Python	             Java
# Constructor	        __init__()	        Constructor
# Current object	    self	            this
# Object creation	    Car()	            new Car()
# Type declaration	    Dynamic	            Static


# 1. Understanding this in Java
# this refers to the current object, not the class itself.

# There are two common situations:
# Case 1: Inside a constructor
# class Student {
#     String name;

#     Student(String name) {
#         this.name = name;
#     }
# }

# Student s1 = new Student("Mohit");


# Here:
# - this refers to the object currently being initialized (s1).
# - this.name refers to the object's instance variable.
# - name refers to the constructor parameter.


# Visualize the assignment
# this.name - (Object variable)   ←  name - (Constructor parameter)

# The parameter's value is assigned to the current object's name variable.

# Case 2: Outside a constructor
# class Student {
#     void display() {
#         System.out.println(this);
#     }
# }

# Student s1 = new Student();
# Student s2 = new Student();

# s1.display();
# s2.display();


# Here:
# - When s1 calls display(), this refers to s1.
# - When s2 calls display(), this refers to s2.
# In other words, this depends on which object calls the method.

# 2. Java this vs Python self
# This is particularly important:
# Java	Python
# this	self
# Implicitly provided	Explicitly declared
# this.name	self.name
# this.display()	self.display()

# Python equivalent:
class Student:    
    def __init__(self, name):        
        self.name = name    
    def display(self):        
        print(self.name)

s1 = Student("Mohit")
s2 = Student("Rahul")

s1.display()
s2.display()

# Python internally passes the calling object as self.

# For example:
s1.display()

# Conceptually becomes:
Student.display(s1)

# In Python, a class can have only one __init__() method definition that acts as its initializer.
# Unlike Java, Python does not support traditional constructor overloading.

# What if you define two constructors in Python?
class Tea:
    def __init__(self):
        print("First constructor")

    def __init__(self, name):
        print("Second constructor")

# t1 = Tea("Masala")  # Works
# t2 = Tea()          # TypeError
# Python does not throw an error here. The second definition overwrites the first one.

class Tea:
    def __init__(self, tea_type="Normal", size="Small"):
        self.tea_type = tea_type
        self.size = size

t1 = Tea()
t2 = Tea("Masala")
t3 = Tea("Green", "Large")

print(t1.tea_type, t1.size)  # Normal Small - Default values are used
print(t2.tea_type, t2.size)  # Masala Small - Default value for size is used
print(t3.tea_type, t3.size)  # Green Large - Both values are provided

# Other ways to achieve constructor-like overloading
# Python also supports:
# - Default arguments
# - *args and **kwargs
# - @classmethod as alternative named constructors