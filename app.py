

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

print('Welcome to the car game\n')
print('You have to enter the command to the car.\n start - car will start\n stop - car will stop\n quit - game will end')
carStatus = input('')

while carStatus != 'quit':
    if carStatus == 'start':
        print('Car started')
    elif carStatus == 'stop':
        print('Car stopped')
    elif carStatus == 'quit':
        print('Game ended')
        break
    else:
        print('I don\'t understand that command')

    carStatus = input('')

