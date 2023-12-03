#!/usr/bin/python3

def is_palendrome(number):
    number_str = str(number)
    
    for i in range(0,len(number_str)):
        if number_str[i] != number_str[-(i + 1)]:
            return False
    return True


def find_top_match(number_of_digits):
    max_value = int("9"*number_of_digits)
    top_match = (0,0,0)

    for i in range(max_value,0,-1):
        for j in range(max_value,0,-1):
            candidate = i * j
            if is_palendrome(candidate) and candidate > top_match[-1]:
                top_match = (i,j,candidate)
    return top_match


def tests():
    assert is_palendrome(123) == False
    assert is_palendrome(12321) == True

    assert find_top_match(2)[-1]==9009
    return("====================\nTests Pass\n====================\n")

if __name__=="__main__":
    print(tests())

    (i, j, maximum) = find_top_match(3)
    
    print(f'Top Match {i} x {j} = {maximum}.')
