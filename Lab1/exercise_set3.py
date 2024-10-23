"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    arr = np.random.randint(0, 10, size=(4, 2))

    print("Array:\n", arr)
    print("Shape:", arr.shape)
    print("Data type:", arr.dtype)
    print("Number of dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Item size:", arr.itemsize)


# ex2
def exercise2():
    arr = np.arange(100, 200, 10).reshape(5, 2)  # Create a 5x2 array with a step of 10
    print("Array:\n", arr)


# ex3
def exercise3():
    arr = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

    third_column = arr[:, 2]
    print("Third column:\n", third_column)


# ex4
def exercise4():
    arr = np.array([[3, 6, 9, 12],
                    [15, 18, 21, 24],
                    [27, 30, 33, 36],
                    [39, 42, 45, 48],
                    [51, 54, 57, 60]])

    odd_rows_even_cols = arr[::2, 1::2]
    print("Odd rows and even columns:\n", odd_rows_even_cols)


# ex5
def exercise5():
    arr1 = np.array([[5, 6, 9], [21, 18, 27]])
    arr2 = np.array([[15, 33, 24], [4, 7, 1]])

    result = arr1 + arr2
    sqrt_result = np.sqrt(result)

    print(sqrt_result)


# ex6
def exercise6():
    arr = np.array([[34, 43, 73],
                    [82, 22, 12],
                    [53, 94, 66]])

    sorted_arr = np.sort(arr, axis=None).reshape(arr.shape)
    print("Sorted array:\n", sorted_arr)


# ex7
def exercise7():
    arr = np.array([[34, 43, 73],
                    [82, 22, 12],
                    [53, 94, 66]])

    max_axis_0 = np.max(arr, axis=0)
    min_axis_1 = np.min(arr, axis=1)

    print("Max along axis 0:\n", max_axis_0)
    print("Min along axis 1:\n", min_axis_1)


# ex8
def exercise8():
    arr = np.array([[34, 43, 73],
                    [82, 22, 12],
                    [53, 94, 66]])

    new_column = np.array([10, 10, 10]).reshape(-1, 1)
    modified_arr = np.delete(arr, 1, axis=1)
    modified_arr = np.insert(modified_arr, 1, new_column, axis=1)

    print("Modified array:\n", modified_arr)


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")
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
