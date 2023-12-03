#!/usr/bin/python3
from math import floor,sqrt

class Prime:
    def __init__(self):
        self.primes = [2,3]
    def get_next_prime(self):
        keep_going = True
        i = self.primes[-1]
        
        while keep_going:
            i+=2
            factors = [prime for prime in self.primes \
                    if pow(prime,2)<=i and i % prime==0]
            if len(factors) == 0:
                keep_going = False
                self.primes = self.primes + [i]
    def get_primes(self, prime_count):
        for i in range(0,prime_count):
            self.get_next_prime()


def tests():
    test_primes = Prime()
    
    test_primes.get_next_prime()
    assert test_primes.primes[-1] == 5

    test_primes.get_primes(100)
    assert 23 in test_primes.primes and 21 not in test_primes.primes
    assert test_primes.primes[5]==13

    return("====================\nTests Pass\n====================\n")

if __name__=="__main__":
    print(tests())
    
    prime_list = Prime()
    prime_list.get_primes(10_000)
    print(f'The 10,001th prime is {prime_list.primes[10000]}.')
