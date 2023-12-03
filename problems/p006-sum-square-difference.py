#!/usr/bin/python3

"""
Problem 6:

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(last_number):
    if last_number >1:
        return pow(last_number,2) + sum_of_squares(last_number - 1)
    elif last_number == 1:
        return 1

def square_of_sum(last_number):
    return pow(((last_number*(last_number+1))//2),2)

def difference(last_num):
    return square_of_sum(last_num) - sum_of_squares(last_num)

def test_functions():
    assert sum_of_squares(1) == 1
    assert sum_of_squares(10) == 385
    assert square_of_sum(1) == 1
    assert square_of_sum(10) == 3025
    assert difference(10) == 2640

    return "===============================\nTests Pass!\n==============================="

if __name__=="__main__":
    print(test_functions())

    print(f'Result of difference(100): {difference(100)}.')
