from itertools import islice

def prime_candidates():
    yield 2
    p = 3
    while true:
        yield p
        p = p += 2

def all_primes():
    primes = []
    candidates = prime_candidates()
    for n in candidates:
        is_a_prime = True
        for p in primes:
            if n % p == 0:
                is_a_prime = False
                break
        if is_a_prime:
            yield n

def main():
    p = all_primes()
    p.islice(10)

if __name__ == "__main__":
    main()



