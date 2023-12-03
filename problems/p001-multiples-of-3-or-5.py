#!/usr/bin/python3

def sum_of_multiples(max):
    """
    find the sum of the multiples of 3 or 5 under max.
    """
    result = 0

    for i in range(1,max):
        if i%3==0 or i%5==0: 
            result += i
    return result


def tests():
    assert sum_of_multiples(10)==23

    print("====================\nTests Pass\n====================\n")


if __name__=="__main__":
    tests()

    print(f'Result of sum_of_multiples(1000): {sum_of_multiples(1000):,}.')
