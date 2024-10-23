"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product


# ex2
def exercise2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    previous_num = 0
    for i in range(num1, num2 + 1):
        current_sum = previous_num + i
        print(f"Current number: {i}, Previous number: {previous_num}, Sum: {current_sum}")
        previous_num = i


# ex3
def exercise3():
    num = list(map(int, input("Enter a list of numbers: ").split()))
    return num[0] == num[-1]


# ex4
def exercise4():
    num = list(map(int, input("Enter a list of numbers: ").split()))
    for n in num:
        if n % 5 == 0:
            print(f"{n} is divisible by 5")


# ex5
def exercise