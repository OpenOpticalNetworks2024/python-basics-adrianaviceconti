"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]

    result = listOne[1::2] + listTwo[0::2]
    print("Third list:", result)


# ex2
def exercise2():
    sampleList = [34, 54, 67, 89, 11, 43, 94]

    element = sampleList.pop(4)
    sampleList.insert(2, element)
    sampleList.append(element)

    print("Modified list:", sampleList)


# ex3
def exercise3():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    chunk_size = len(sampleList) // 3

    chunk1 = sampleList[:chunk_size][::-1]
    chunk2 = sampleList[chunk_size:chunk_size * 2][::-1]
    chunk3 = sampleList[chunk_size * 2:][::-1]

    print("Chunks reversed:", chunk1, chunk2, chunk3)


# ex4
def exercise4():
    sampleL