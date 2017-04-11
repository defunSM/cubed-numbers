#!/usr/bin/env python
import numpy as np
from optparse import OptionParser

def make_nums(a, b):
    """
    Generates numbers depending on initial conditions given to the make_nums function acting as a range like in clojure and returning a list.

    """

    array = []
    for i in range(a, b):
        array.append(i)

    return array

def raise_nums(array, power):

    raise_array = []
    for i in array:
        raise_array.append(pow(i, power))

    return raise_array


def four_nums(array):
    """
    Raises all numbers in the array to the fourth power. Returns the array after.
    """

    fourth_array = []
    for i in array:
        fourth_array.append(pow(i, 4))

    return fourth_array

def cube_nums(array):
    """
    Cubes all the numbers in the array. Returning that array after.
    """

    cubed_array = []
    for i in array:
        cubed_array.append(pow(i, 3))

    return cubed_array

def square_nums(array):
    """
    Squares all the numbers in the array. Return the array afterwards.
    """

    squared_array = []
    for i in array:
        squared_array.append(pow(i, 2))

    return squared_array

def difference_from_previous(array):
    """
    Calculates the difference from the previous element. Hence calculates the difference.
    """

    length = len(array)
    diff_array = []

    for i in range(0, length-1):
        diff_array.append(array[i+1]-array[i])

    return diff_array

def streamline(start, stop, power, show):
    """
    This is the most top level function which will display everything and call the other helper functions.

    Start - The number that will start the initial array.
    Stop - The number that will end the initial array.
    Power - The power that each element in the array will be raised to.
    show - How many levels of differences will be shown.
    """

    nums = make_nums(start, stop)
    values = raise_nums(nums, power)


    print(values)
    for i in range(0,show):

        new_array = difference_from_previous(values)

        print(new_array)
        values = new_array

def main():
    """
    main function that will call the most top level function which is streamline.
    """

    parser = OptionParser()
    parser.add_option("-s", "--start", help="Number starting the initial array.")
    parser.add_option("-e", "--end", help="Number ending the initial array.")
    parser.add_option("-p", "--power", help="The power that each element in the array will be raised to.")
    parser.add_option("-l", "--levels", help="How many levels od differences will be shown.")

    options, arguments = parser.parse_args()
    start = int(options.start)
    stop = int(options.end)
    power = int(options.power)
    levels = int(options.levels)

    streamline(start, stop, power, levels)  # Start, stop, power, show

if __name__=="__main__":
    main()
