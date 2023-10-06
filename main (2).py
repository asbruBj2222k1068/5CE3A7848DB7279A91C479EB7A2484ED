Open In App
Related Articles
Write an Interview Experience
Share Your Campus Experience
Python | Implementing 3D Vectors using dunder methods
Polymorphism in Python
Instance method in Python
__subclasscheck__ and __subclasshook__ in Python
Python | Get the real time currency exchange rate
Python issubclass()
Inheritance in Python Inner Class
Getter and Setter in Python
Types of inheritance Python
Python program to check if a string contains all unique characters
How to Get a List of Class Attributes in Python?
Python – Access Parent Class Attribute
Protein structure prediction in Cloud Computing
Pros and Cons of URL Shorteners
Coding the Financial Market
Check if the binary representation of a number has equal number of 0s and 1s in blocks
Python | Sort list of dates given as strings
Is downloading YouTube videos legal?
Microarchitecture and Instruction Set Architecture
Token Bus (IEEE 802.4)
Python Program to Convert a List to String
Defaultdict in Python
Python | Get dictionary keys as a list
Python | Split string into list of characters
How to print without newline in Python?
Python Program to Check Prime Number
Convert a List to Dictionary Python
Python Program to Print the Fibonacci sequence
Convert String Dictionary to Dictionary Python
Python Program for Binary Search (Recursive and Iterative)
Python program to create Bankaccount class with deposit, withdraw function
M

mohinish10
Read
Discuss
Courses
Video
Prerequisite: Object Oriented Programming in Python
Let’s write a simple Python program using OOP concept to perform some simple bank operations like deposit and withdrawal of money.
First of all, define class Bankacccount. This step is followed by defining a function using __init__. It is run as soon as an object of a class is instantiated. This __init__ method is useful to do any initialization you want to do with object, then we have the default argument self.
 

Python3
# BankAccount class
class Bankaccount:
    def __init__(self):
This step is followed by declaring that balance is 0 using self argument then we simply print a statement welcoming to Machine. In function deposit and withdraw , amount is taken as input(in float) and is then added/subtracted to the balance. Thus resultant balance is printed in next line.
 

Python3
# Function to deposit amount
def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
Use an if condition to check whether there is a sufficient 
amount of money available in the account to process a fund withdrawal.
 

Python3
# Function to withdraw the amount
def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
Next, we use a display function to display the remaining balance in the account. Then we create a object and call it to get the program executed. 
 

Python3
# Function to display the amount
def display(self):
        print("\n Net Available Balance =", self.balance)
Below is the implementation: 
 

Python3
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()Open In App
Related Articles
Write an Interview Experience
Share Your Campus Experience
Python | Implementing 3D Vectors using dunder methods
Polymorphism in Python
Instance method in Python
__subclasscheck__ and __subclasshook__ in Python
Python | Get the real time currency exchange rate
Python issubclass()
Inheritance in Python Inner Class
Getter and Setter in Python
Types of inheritance Python
Python program to check if a string contains all unique characters
How to Get a List of Class Attributes in Python?
Python – Access Parent Class Attribute
Protein structure prediction in Cloud Computing
Pros and Cons of URL Shorteners
Coding the Financial Market
Check if the binary representation of a number has equal number of 0s and 1s in blocks
Python | Sort list of dates given as strings
Is downloading YouTube videos legal?
Microarchitecture and Instruction Set Architecture
Token Bus (IEEE 802.4)
Python Program to Convert a List to String
Defaultdict in Python
Python | Get dictionary keys as a list
Python | Split string into list of characters
How to print without newline in Python?
Python Program to Check Prime Number
Convert a List to Dictionary Python
Python Program to Print the Fibonacci sequence
Convert String Dictionary to Dictionary Python
Python Program for Binary Search (Recursive and Iterative)
Python program to create Bankaccount class with deposit, withdraw function
M

mohinish10
Read
Discuss
Courses
Video
Prerequisite: Object Oriented Programming in Python
Let’s write a simple Python program using OOP concept to perform some simple bank operations like deposit and withdrawal of money.
First of all, define class Bankacccount. This step is followed by defining a function using __init__. It is run as soon as an object of a class is instantiated. This __init__ method is useful to do any initialization you want to do with object, then we have the default argument self.
 

Python3
# BankAccount class
class Bankaccount:
    def __init__(self):
This step is followed by declaring that balance is 0 using self argument then we simply print a statement welcoming to Machine. In function deposit and withdraw , amount is taken as input(in float) and is then added/subtracted to the balance. Thus resultant balance is printed in next line.
 

Python3
# Function to deposit amount
def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
Use an if condition to check whether there is a sufficient 
amount of money available in the account to process a fund withdrawal.
 

Python3
# Function to withdraw the amount
def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
Next, we use a display function to display the remaining balance in the account. Then we create a object and call it to get the program executed. 
 

Python3
# Function to display the amount
def display(self):
        print("\n Net Available Balance =", self.balance)
Below is the implementation: 
 

Python3
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()