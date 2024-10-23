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
def exercise5():
    input_string = "Emma is a good developer. Emma is also a writer."
    return input_string.count("Emma")


# ex6
def exercise6():
    list1 = list(map(int, input("Enter a list of numbers: ").split()))
    list2 = list(map(int, input("Enter another list of numbers: ").split()))
    result_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
    return result_list


# ex7
def exercise7():
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")
    middle_index = len(s1) // 2
    return s1[:middle_index] + s2 + s1[middle_index:]


# ex8
def exercise8():
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")

    def get_middle_char(s):
        return s[len(s) // 2] if len(s) % 2 != 0 else s[(len(s) // 2) - 1]

    result = s1[0] + get_middle_char(s1) + s1[-1] + s2[0] + get_middle_char(s2) + s2[-1]
    return result


# ex9
def exercise9():
    input_string = input("Enter a string: ")
    lower_count = sum(1 for c in input_string if c.islower())
    upper_count = sum(1 for c in input_string if c.isupper())
    digit_count = sum(1 for c in input_string if c.isdigit())
    special_count = sum(1 for c in input_string if not c.isalnum())

    return {"lowercase": lower_count, "uppercase": upper_count, "digits": digit_count, "special symbols": special_count}


# ex10
def exercise10():
    input_string = input("Enter a string: ")
    return input_string.lower().count("usa")


# ex11
def exercise11():
    input_string = input("Enter a string: ")
    digits = [int(char) for char in input_string if char.isdigit()]
    total_sum = sum(digits)
    average = total_sum / len(digits) if digits else 0
    return {"sum": total_sum, "average": average}


# ex12
def exercise12():
    input_string = input("Enter a string: ")
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()