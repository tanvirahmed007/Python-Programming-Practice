

# This is for understanding the functions and how it works.........................

# basic

# def tanvir():
#     print("\nHello Tanvir\n")

# tanvir()


# with arguments

# def tanvir(firstname, lastname):
#     print("\nHello {} {}\n".format(firstname, lastname))

# tanvir("Tanvir", "Ahmed")

# alternative way

# def tanvir(firstname, lastname):
#     print("\nHello {} {}\n".format(firstname, lastname))


# tanvir("Tanvir", "Ahmed")


# incremental arguments

# def increment(num1, num2):
#     return num1 + num2

# # result = increment(2, 3)
# # print(result)

# print(increment(2, 3))


# *args, wait, what===================

# def multiply(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total

# print(multiply(2, 3, 4, 5))


# **args

# def info(**kwargs):
#     print(kwargs["name"])

# info(id=1, name="Tanvir", age=22)


# Fizz Buzz=======================

# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     if num % 5 == 0:
#         return "Buzz"
    
#     return num

# print(fizzbuzz(int(input("Enter a number: "))))

