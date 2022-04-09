

#data type ===============================================

# int

# num = 10
# print(f'int type: {num}')


# float

# num2 = 10.5
# print(f'float type: {num2}')


# basic numeric operations

# x = 10
# y = 5

# print(f'x + y = {x + y}')
# print(f'x - y = {x - y}')
# print(f'x * y = {x * y}')
# print(f'x / y = {x / y}')

# power
# print(f'x ** y = {x ** y}')

# remain
# print(f'x % y = {x % y}')


# string
# fname = 'Tanvir'
# lname = 'Ahmed'

# print(f'{fname} {lname}')


# under the hood unicode

# s1 = chr(97)
# s2 = chr(98)
# s3 = chr(99)
# print(s1+s2+s3)


# escape character =========================================

# \n new line
# \t tab
# \b backspace
# \r new line
# \ appostrophe


# input from user and print ==========================================

# name = input('Enter your name: ')
# print(f'Hello {name}')


# string concatenation

# birthYear = input('Enter your birth year: ')
# age = 2022 - int(birthYear)
# print(f'Your age is {age}')


# string ====================================================
# multiple line string

# message = '''
# Hello, Myself Tanvir Ahmed from Bangladesh.

# I am a Software Engineer. And I am learning Python.

# Thank you.

# '''

# print(message)


# string format

# fname = 'Tanvir'
# lname = 'Ahmed'

# print(f'Hello {fname} {lname}')


# string methods

# name = 'Tanvir Ahmed'
# print(len(name)) # length method

# print(name.upper()) # upper method

# print(name.lower()) # lower method

# print(name.title()) # title method

# print(name.count('a')) # count method

# print(name.find('a')) # find method

# print(name.replace('a', 'A')) # replace method

# print('Tanvir' in name) # in method will return true or false



# Arithmetic Operators================================================

# x = 10
# Y = 5

# print(f'x + Y = {x + Y}')
# print(f'x - Y = {x - Y}')
# print(f'x * Y = {x * Y}')
# print(f'x / Y = {x / Y}')
# print(f'x ** Y = {x ** Y}')
# print(f'x % Y = {x % Y}')
# print(f'x // Y = {x // Y}')

# # math functions
# import math

# x = 10.4
# print(f'round(x) = {round(x)}')
# print(f'abs(x) = {abs(-x)}') # absolute value
# print(f'ceil(x) = {math.ceil(x)}') # ceil method


# if else statement===============================================

# is_hot = False
# is_cold = True

# if is_hot:
#     print('It is hot')
# elif is_cold:
#     print('It is cold')
# else:
#     print('It is not hot and cold')


# credit = input('Is your credit good? yes or no?: ')
# price = 1000000

# if credit == 'yes':
#     down_payment = price * 0.1
#     print('You need to put 10% which is {}'.format(down_payment))

# elif credit == 'no':
#     down_payment = price * 0.2
#     print('You need to put 20% which is {}'.format(down_payment))

# print('The down payment is {}. Thank you'.format(down_payment))


# temp = int(input('Enter the temperature: '))

# if temp>30:
#     print('It is hot')

# elif temp<30:
#     print('It is cold')

# else:
#     print('It is normal')


# name = input('Enter your name: ')



# if len(name) < 3:
#     print('Name must be at least 3 characters long')    

# elif len(name) > 50:
#     print('Name must be less than 50 characters long')

# else:
#     print('Name is valid')


# while loop ======================================================

# num = int(input('Enter a number: '))
# while num < 10:
#     print(num)
#     num += 1

# print('Done')


# guessing game ======================================================

# secretNumber = 7
# guessLimit = 3
# guessCount = 0

# while guessCount < guessLimit:
#     guess = int(input('Guess: '))
#     guessCount += 1

#     if guess == secretNumber:
#         print('You won!')
#         break
#     else:
#         print('You failed! Try again')


# car game ======================================================

# print('Welcome to the car game\n')
# print('You have to enter the command to the car.\n start - car will start\n stop - car will stop\n quit - game will end')
# carStatus = input('')

# while carStatus != 'quit':
#     if carStatus == 'start':
#         print('Car started')
#     elif carStatus == 'stop':
#         print('Car stopped')
#     elif carStatus == 'quit':
#         print('Game ended')
#         break
#     else:
#         print('I don\'t understand that command')

#     carStatus = input('')


# for loop ======================================================
# for item in ['Python', 'Java', 'C++']:
#     print(item)


# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)

# for item in range(0, 10, 2):
#     print(item)


# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f'Total: {total}')

# nested loop==============

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# numbers = [2, 2, 2, 2, 5]

# for item in numbers:
#     output = ''
#     for num in range(item):
#         output += 'x'
#     print(output)


numbers = [12, 46, 33, 23, 2]

# for item in numbers:
#     output = max(numbers)
# print(output)

# # other way

# maxNumber = numbers[0]
# for item in numbers:
#     if item > maxNumber:
#         maxNumber = item
# print(maxNumber)


# 2D list===========================================================

# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(numbers)
    
# list methods ======================================================

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers.append(11) # add item to the end of the list
# numbers.insert(0, 0) # insert item at the specified index
# numbers.remove(11) # remove item from the list
# numbers.pop() # remove last item from the list
# numbers.clear() # remove all items from the list
# numbers.index(5) # return the index of the item

# print(numbers.count(5)) # return the number of times the item appears in the list
# print(numbers.sort()) # sort the list
# print(numbers.reverse()) # reverse the list
# print(numbers)

# numbers2 = numbers.copy() # copy the list
# print(numbers2)


# numbers = [1, 2, 2, 6, 3, 4, 5, 6, 7, 8, 9, 10]
# unique = []
# for item in numbers:
#     if item not in unique:
#         unique.append(item)
# print(unique)


# tuples ============================================================

# numbers = (1, 2, 3, 4)
# x, y, z, t = numbers
# print('x = {}, y = {}, z = {}, t = {}'.format(x, y, z, t))


# dictionary ============================================================

# customer = {
#     'name': 'John Smith',
#     'age': 30,
#     'is_verified': True
# }

# print(customer['name'])
# print(customer.get('birthdate', 'Jan 1 1980'))
# print(customer['age'])
# print(customer['is_verified'])
# print(customer)



# emoji converter ===========================

# message = input('> ')
# words = message.split(' ')
# emojis = {
#     ':)': '😊',
#     ':(': '😞'
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
    
# print(output)


# function ============================================================

# def index():
#     print('Welcome to the homepage')


# index()

# parameters =============
# def greet(name, greeting):
#     print(f'{greeting} {name}')


# greet("Tanvir","Welcome") # parameters



# classes ====================================================
# class Point:
#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()



# constructor ===================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')


# point1 = Point(101, 102)

# print(point1.y)
# point1.draw()



# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'Hi, I am {self.name}')


# person1 = Person('Tanvir')
# person1.talk()



# modules ========================================================
from convert import kgToLbs

result = kgToLbs(100)

print(result)

