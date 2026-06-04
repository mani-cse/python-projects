# def check_armstrong(number):
#     total_digit = len(str(number))
#     total = 0
#     for digit in str(number):
#         total += int (digit) ** total_digit
#     if total == number:
#         print("Armstrong")
#     else:
#         print("Not Armstrong")
# check_armstrong(153)
# check_armstrong(370)/
# numbers = [34,12,89,5,67,23,90,35]
# def find_largest(number):
#     largest = number[0]
#     for num in numbers:
#         if num > largest :
#             largest = num
#     return largest
# result = find_largest(numbers)
# print("largest value:",result)
# def calculate_si(principal,rate,time):
#     si = (principal * rate * time) / 100
#     return si
# print("First value:",calculate_si(10000,5,3))
# print("Second value:",calculate_si(5000,8,2))
# print("Third value:",calculate_si(50000,4,7))
# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1)
# print("Factorial of 5:",factorial(5))
# print("Factorial of 8:",factorial(8))
# def greet (name,language = "English"):
#     if language == "English":
#         print("Hello",name)
#     elif language == "Tamil":
#         print("Vanagam",name)
#     elif language == "Hindi":
#         print("Namaste",name)
# greet("Macha!")
# greet("Macha!","Tamil")
# greet("Macha!","Hindi")
# class student:
#     def __init__(self,name,age,dept):
#         self.name = name
#         self.age = age
#         self.dept = dept
#     def introduce(self):
#         print("Hi I am",self.name,self.age,"Years old","Studying",self.dept)
# s1 = student("Mani",21,"CSE")
# s2 = student("Loki",20,"EEE")
# s3 = student("Magesh",22,"DOCTOR")
# s1.introduce()
# s2.introduce()
# s3.introduce()
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print("Blanace after Deposit:",self.balance)
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Balance !")
#         else:
#             self.balance -= amount
#             print("Balance after withdrawal:",self.balance)
#     def check_balance(self):
#         print("Current Balance",self.balance)
# acc1 = BankAccount("Mani",10000)
# acc1.deposit(5000)
# acc1.withdraw(3000)
# acc1.check_balance()
# acc1.withdraw(50000)
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(self.name,"is eating")
# class dog (Animal):
#     def speak(self):
#         print(self.name,"says: woof!")
# class cat (Animal):
#     def speak(self):
#         print(self.name,"says: Meow !")
# d1 = dog("Tommy")
# d1.speak()
# d1.eat()
# c1 = cat("Pussy")
# c1.speak()
# c1.eat()
# class student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.__mark = mark #(__ double undersore) is private method in python
#     def  display(self):
#         print("Name is",self.name)
#         print("Marks:",self.__mark)
#     def update_mark(self,new_mark):
#         if new_mark >= 0 and new_mark <= 100:
#             self.__mark = new_mark
#             print("Mark updated to:",self.__mark)
#         else:
#             print("Invalide Mark !")
#     def update_name(self,new_name):
#         self.name = new_name
#         print("upated new name:",self.name)
# s1 = student("Mani",85)
# s1.display()
# s1.update_mark(95)
# s1.display()
# s1.update_name("Loki")
# s1.display()
# print(s1.__mark)
class circule:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Area of Circule:",3.14 * self.radius ** 2)
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of Rectangle:",self.length * self.width)
class Triangle:
    def __init__(self,base,hight):
        self.base = base
        self.hight = hight
    def area(self):
        print("Area of Triangle:",0.5 * self.base * self.hight)
c1 = circule(7)
r1 = Rectangle(10,5)
t1 = Triangle(6,4)

c1.area()
r1.area()
t1.area()