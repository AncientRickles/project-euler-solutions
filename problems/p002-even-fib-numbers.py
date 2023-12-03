#!/usr/bin/python3

class Fib:
    def __init__(self):
        self.fib = [1,1]

    def generate_next(self):
        self.fib = self.fib + [self.fib[-2]+self.fib[-1]]

    def generate_to(self, limit):
        while self.fib[-1] < limit:
            self.generate_next()


def tests():
    test_fib = Fib()
    test_fib.generate_next()
    assert test_fib.fib[-1] == 2
    test_fib.generate_to(100)
    assert 89 in test_fib.fib
    return("====================\nTests Pass\n====================\n")


if __name__=="__main__":
    print(tests())

    euler_fib = Fib()

    euler_fib.generate_to(4_000_000)

    sum = 0

    even_fib = [num for num in list(euler_fib.fib) if num%2==0 and num < 4_000_000]

    for number in even_fib: sum += number

    print(f'Result - Sum of even fibonacci numbers under 4,000,000: {sum:,}')
