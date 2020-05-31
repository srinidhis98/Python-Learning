
import math
#print("Hello world")
#print('$'* 2)

#name =""
#age = 0
# name =input("enter the patient name:")
# age = input ("enter the patient's age")
# if (name == "john" and age == 20):
#     print ("he is a new patient")
# else:
#     print("he is existing patient")

# name = input("What is your name? ")
# color = input("what is favorite color? ")
# print (name+" likes "+color)
# birth_year = input ("Birth year:")
# #print(type(birth_year))
# age = 2020 - int(birth_year)
# print('Your age is ' ,age)


# weight_lbs = input('Enter the weight: ')
# weight_kgs = float(weight_lbs) * 0.45
# print(weight_kgs)


# day = input('Hows the weather: ')
# if ( day == 'hot' ):
#     print("Its a hot day"+"\n"+"Drink plenty of water")
# elif (day == 'cold'):
#     print ("It's a cold day"+"\n"+ 'Wear warm clothes')
# else:
#     print ("Have a nice day")
#

# price = 5234512
# if (price > 1000):
#     down_payment = 0.1 * price
# elif (price < 1000):
#     down_payment = 0.2 * price
#  #   print("total payment is done")
# print(f'Down payment is ${down_payment}')




# temp = input("enter the temperature")
# if (int(temp) >30):
#     print("its a hot day")
# elif(int(temp) < 10):
#     print("its a cold day")
# else:
#     print("its neither hot nor cold")


# name = input("enter a name")
#
# if (len(name) < 3):
#     print("name must be atleast 3 char long")
# elif (len(name)>50):
#     print("name can be maximum of 50 char long")
# else:
#     print("name looks good")

#
# weight = input("enter your weight")
# unit = input("L(bs) or K(g)")
# if (unit == "L" or unit =="l"):
#     weight = int(weight)*0.453592
#     print(f'Your weight is {weight} kilograms')
# else:
#     weight = int(weight)/0.453592
#     print(f'Your weight is {weight} pounds')




# command = ""
# while command.lower() != "quit":
#     command = input("> ")
#     if (command.lower() == "help"):
#         print (" start - start the car \n stop - stop the car \n quit - quit the game")
#     elif (command.lower() == "start"):
#         print ("Car is started")
#     elif (command.lower() =="stop"):
#         print ("Car is stopped")
#     elif (command.lower() == "quit"):
#         break
#     else:
#         print ("Command not supported")




# time = input("Get the I

# for char in 'Srinidhi Sivakumar':
#     print(char)
#



# for item in ['srinidhi', 'sivakumar', 'banurekha', 'nandhini', 'barath', 'renuga', 'balasubramanian', 'aadhitya', 'priyadarshan']:
#     print(item)
#


# for item in range(2,11,2):
#     print(item)

# prices = []
# total = 0
# items = int(input("enter the number of items in shopping cart"))
# for i in range(0,items,1):
#     item = int(input())
#     prices.append(item)
#     total=total+item
#
# print(total)

#
# for x in range(0,3,1):
#     for y in range(0,3,1):
#         print(f'({x},{y})')
#

num = [2,2,2,2,5,5]

# for i in num:
#     for j in range(i):
#         print ("X", end=" ")
#     print()

# names =['srinidhi', 'sivakumar','bannurekha','nandhini']
# print(names[:3])


# numbers = [123, 345, 5671, 400000, 35400]
# big_num = 0
# for num in numbers:
#     if(big_num < num):
#         big_num = num
#     elif (big_num > num):
#         continue
#
# print(big_num)


# matrix =[[1,2,3],[4,5,6],[7,8,9]]
# mat_len = len(matrix)
# #print(type(mat_len))
# # for i in matrix:
# #     for j in matrix[]:
# #         print(j)
# #     # row_len = len(i)
# #     # for j in range(row_len):
# #     #     print(j, end=" ")
# #     # print(i)
# #
# for row in matrix:
#     for col in row:
#         print(col, end =" ")
#     print()


# numbers = [1,2,3,4,5,8,9,0,1,3,5,23,23,25,26,25,500,35,500,75,75,80,89,697,666,5500,55500,0,55500]
#
# # for num in numbers:
# #    # print(numbers.count(num))
# #     if(numbers.count(num) > 1):
# #         numbers.remove(num)
# #         print(numbers)
# # numbers.sort()
# # print(numbers)
#
# unique = []
# for num in numbers:
#     if(num not in unique):
#         unique.append(num)
# print(unique)

#
coordinates = (1,2,3,4)
print(coordinates)
a,b,c,d = coordinates ##unpacking both for tuples and lists
print (a+b+c+d)


#dictionaries
# employee = {
#     "Name" : "Srinidhi",
#     "Company": "VMware",
#     "ID" : 392689,
# }
# employee["dob"] = "14 Nov 1998"
# print(employee.get('Name'))
# print(employee)

# name = {
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:'six',
#     7:"seven",
#     8:'eight',
#     9:'nine',
#     0:'zero'
# }
#
# phone = input("Phone: ")
# for i in phone:
#     print(name.get(int(i)), end= " ")


# message = input('>')
# words = message.split(' ')
# #print(words)
# emojis = {
#     ':)' : '🙂',
#     ':(' : '🙁'
# }
# convert = " "
# for word in words:
#    convert = convert + " " + emojis.get(word, word)
#
# print(convert)



# def greet(fname, lname):
#     print(f'Hello {fname} {lname}')
#     print("Please be patient")
#     fname = 'Priyadarshan'
#     return fname
#
# name_ret=greet(lname = "Sivakumar",fname = 'Srinidhi')
# print(name_ret)

# try:
#     age = int(input("Enter your age"))
#     print(f'Your age is {age}')
# except ValueError:
#     print('Invalid Error')



# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def move_point(self):
#         print("point is moved thru this function")
#
#
#     def draw_line(self):
#         print("this function is used to draw lines")
#
# point_obj = Point(10,20)
# print(point_obj.a)
# point_obj.var1 = 100
# print(point_obj.var1)
# point_obj.draw_line()
# point_obj.move_point()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'{self.name} is talking  now')
#
#
# srini = Person("Srinidhi")
# print(f'Name of the Personn object: {srini.name}')
# srini.talk()
#
# priyadarshan = Person("Priyadarshan")
# print(priyadarshan.name)
# priyadarshan.talk()


#Inheritance

# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# class Dog(Mammal):
#     def walk(self):
#         print('dog is walking')
#
# class Cat(Mammal):
#     pass
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.walk()

# one method of importing function from the package
# import ecomm1.shipping
# ecomm1.shipping.calc_shipping()

#another way of importing funnction from a package
# from ecomm1.shipping import calc_shipping
# calc_shipping()


# import random
# for i in range(3):
#     print(random.randint(10,2000))


import random

members = ['srinidhi', 'aadhitya', 'priyadarshan', 'sivakumar']
leader = random.choice(members)
print(leader)


# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return (first, second)
#
#
# dice1 = Dice()
# print(dice1.roll())
#

# from pathlib import Path
#
# # path = Path('ecomm1')
# # print(path.exists())
# # path = Path("application")
# # #path.mkdir()
# # path.rmdir()
#
# path = Path()
# # print (path.glob("*.py"))
# for file in path.glob("*.py"):
#     print(file)


# import openpyxl as xl
# wb = xl.load_workbook("transactions.xlsx")
# sheet = wb["Sheet1"]
# cell = sheet.cell(1,1)
# # print(cell.value)
# print(sheet.max_row)
#
# for row in range(2, sheet.max_row + 1):
#     # print(row)
#     cell = sheet.cell(row,3)
#     print(cell.value)
#     correct_val = cell.value * 0.9
#     cell1 = sheet.cell(row,4)
#     cell1.value = correct_val
#     # print(cell1.value)
#
# wb.save("transaction2.xlsx")