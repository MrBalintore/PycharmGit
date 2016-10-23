__author__ = 'david'
from itertools import islice
from math import sqrt
def prime_candidates():
    yield 2
    p = 3
    while True:
        yield p
        p += 2

def all_primes():
    primes = []
    candidates = prime_candidates()
    for n in candidates:
        is_a_prime = True
        for (p,p2)  in primes:
            #print n, p, p2
            if ( p2 >= n ): # 6328 instead of 283 if omitted
               break
            if (n % p == 0): # or p > sqrt(n) :
                is_a_prime = False
                break
        if is_a_prime:
            primes.append( (n, n * n) )
            yield n

def main():
    
    for i in range(5):
        p = all_primes()
        n = pow(10,i)
        print n
        ten = list( islice(p,n-1,n+9,1) )
        print ten
        print ten[0] / float(n)

if __name__ == "__main__":
    main()

