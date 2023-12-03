#!/usr/bin/python3

from math import floor,sqrt

def find_factor(number):
    ceiling = floor(sqrt(number))
    
    factors = [i for i in range(3, ceiling+1,2) if number % i == 0]
    
    if number % 2 == 0: factors = [2] + factors

    if len(factors) == 0: 
        factors += [number]
    return sorted(factors)[0]

def factorize(number):
    left_over = number
    factors = []

    while left_over > 1:
        factor = find_factor(left_over)
        factors += [factor]
        left_over = left_over // factor
    return sorted(factors)

def tests():
    assert find_factor(6) == 2
    assert find_factor(49) == 7
    
    assert factorize(13195) == [5,7,13,29]
    return("====================\nTests Pass\n====================\n")


if __name__=="__main__":
    print(tests())
    
    test_number = 600851475143
    factors = factorize(test_number)

    print(f'Factors of {test_number:,}: {factors}\nLargest Prime Factor: {factors[-1]}')
