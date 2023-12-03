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


def find_smallest_multiple(number_range):
    prime_factors_list = []
    for i in number_range:
        factors = factorize(i)

        for factor in set(factors):
            while factors.count(factor) > prime_factors_list.count(factor):
                prime_factors_list += [factor]

    product = 1
    for factor in prime_factors_list:
        product *=factor
    return product


def tests():
    assert find_factor(6) == 2
    assert find_factor(49) == 7                                    
                                                                      
    assert factorize(13195) == [5,7,13,29]     

    assert find_smallest_multiple(range(1,11))==2520
    
    return("====================\nTests Pass\n====================\n")

if __name__=="__main__":
    print(tests())

    product = find_smallest_multiple(range(1,21))

    
    print(f'The smallest number evenly divisible by 1 - 20 is {product}.')
