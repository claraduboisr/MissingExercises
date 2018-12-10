##### Random Sum

import random
number = 0
for i in range(10):
    number += random.randint(0, 100)
print(number)

#####

def test(number, odd=True):

    if odd:
        if number % 2 == 0:
            odd = False
    else:
        if number % 2 == 1:
            odd = False
    return odd
num = int(input("Input a number "))
if test(num):
    print("The number is odd.")
else:
    print("The number is even.")

##### Write a function that creates a list of random number of random numbers

import random
def new_list():
    a = []
    for i in range (0,1000):
        number = random.randint(0,1000)
        a.append(number)
    return a
my_list = new_list()
my_list.sort()
print(my_list[-1]) #-1: you get the last element of the list

##### Write a function that finds the maximum for the above list, write a function that sorts the above list, write another function that sort it (different algorithm)

import random
import time


def new_list():
    temp = []
    for i in range(random.randint(1, 1000)):
        temp.append(random.randint(0, 1000))

    return temp


# I don't use sort and then [-1] because that edits the actual list
def find_max(arg_list=[]):
    temp = arg_list[0]
    pos = 0

    for i in range(len(arg_list)):
        if arg_list[i] > temp:
            temp = arg_list[i]
            pos = i

#   return temp  # Not as important
    return pos


def my_sort(arg_list=[]):

    result = []
    while len(arg_list) > 0:
        pos = find_max(arg_list)
        result.insert(0, arg_list.pop(pos))

    return result


def insert(arg_list=[]):

    for i in range(len(arg_list)):
        for j in range(i):
            if arg_list[i] < arg_list[j]:
                temp = arg_list[i]
                arg_list[i] = arg_list[j]
                arg_list[j] = temp

    return arg_list


my_list = new_list()
# my_list = [360, 433, 720, 840, 126, 380]  # For testing purposes
print(my_list)

result = my_sort(my_list.copy())
print(result)

result = insert(my_list.copy())
print(result)

