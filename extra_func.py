from gmpy2 import mpz, powmod
from sympy import isprime

def is_primitive_root_of_unity(g, n, modulus):
    
    g = mpz(g)
    n = mpz(n)
    modulus = mpz(modulus)

    if powmod(g, n, modulus) != 1:
        return False

    d = 1
    while d * d <= n:
        if n % d == 0:
            if powmod(g, d, modulus) == 1:
                return False
            if d != 1 and d != n // d:
                if powmod(g, n // d, modulus) == 1:
                    return False
        d += 1

    return True

def find_primitive_root_of_unity4(n, modulus):
    assert isprime(modulus), "Modulus must be prime"
    candidate = mpz(2)
    while candidate < modulus:
        if powmod(candidate, n, modulus) == 1:  # Ensure g^n ≡ 1 (mod q)
            # Check that it does not satisfy the condition for any proper divisor of n
            all_good = True
            d = 1
            while d * d <= n:
                if n % d == 0:  # d is a divisor of n
                    # Check if it satisfies g^d ≡ 1 (mod q) for divisor d
                    if powmod(candidate, d, modulus) == 1:
                        all_good = False
                        break
                    # Check the quotient of n / d if it is a distinct divisor
                    if d != 1 and d != n // d:
                        if powmod(candidate, n // d, modulus) == 1:
                            all_good = False
                            break
                d += 1
            if all_good:
                return candidate  # This candidate is a valid primitive root of unity
        candidate += 1
    return None  # No primitive root found

def gen_uniform_database(size, modulus):
    
    # Create a random state object
    rand_state = random_state(int(time.time()))

    # Generate coefficients using gmpy2, keeping them as mpz objects
    coefficients = [mpz(gmpy2.mpz_random(rand_state, modulus)) for _ in range(size)]
    return coefficients
