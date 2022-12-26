#import std
import math
import random
import argparse
from argparse_range import range_action

def main():
    parser = argparse.ArgumentParser(
                    prog = 'project',
                    description = 'Generates randon prime number with given digits',
                    epilog = 'Created by Akhil Agarwal (er.akhilagarwal@gmail.com)')
    parser.add_argument('-d', '--digits',
                    action=range_action(1, 300),
                    #type=int, min=1, max=300,
                    metavar="[1-300]", default = 10,
                    help ="Number of digits for prime number. Default is 10")
    args = parser.parse_args()
    n = generate_random_with_digits(args.digits)
    while(not(is_prime(n))):
        n = generate_random_with_digits(args.digits)
    print(n)

def generate_random_with_digits(digits : int) -> int:
    return random.randint(smallest_n(digits), largest_n(digits))

def smallest_n(digits: int) -> int:
    if digits == 1:
        return 0
    return 10 ** (digits - 1)

def largest_n(digits : int) -> int:
    return (10 ** digits) -1

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if not(n & 1):
        return False
    if is_perfact_square(n):
        return False
    return is_pseudo_prime(n) and is_lucas_pseudo_prime(n)

def is_perfact_square(n):
    import math
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n

def is_pseudo_prime(n: int) -> bool:
    return is_pseudo_prime_base(n, 2) and is_pseudo_prime_base(n, 3)

def is_pseudo_prime_base(n: int, base:int) -> bool:
    exp = n-1
    residue = power(base, exp, n)
    while not(exp & 1) and residue == 1:
        exp //= 2
        residue = power(base, exp, n)
    if ((exp & 1) and residue == 1) or residue == n-1:
        return True
    else:
        return False

# Effectively calculate (x^y) modulo mod
def power(x :int, y :int, mod: int) -> int:
    # Initialize result
    res = 1
    while (y):
        # If power is odd, then update the answer
        if (y & 1):
            res = (res * x) % mod
        # Square the number and reduce
        # the power to its half
        y = y >> 1
        x = (x * x) % mod
    # Return the result
    return res

def is_lucas_pseudo_prime(n: int) -> bool:
    d, p, q = selfridge(n)
    if p == 0: return n == d
    u, v, k = lucas_PQ(p, q, n, n+1)
    return u == 0

def selfridge(n) -> set:
    d, s = 5, 1
    while True:
        ds = d * s
        if gcd(ds, n) > 1:
            return ds, 0, 0
        if jacobi(ds, n) == -1:
            return ds, 1, int((1 - ds) / 4)
        d, s = d + 2, s * -1

def lucas_PQ(p: int, q: int, m: int, n: int) -> set:
    # nth element of lucas sequence with
    # parameters p and q (mod m); ignore
    # modulus operation when m is zero
    def mod(x : int):
        if m == 0: return x
        return x % m
    def half(x : int):
        if x & 1:
            x = x + m
        return mod(x // 2)
    un, vn, qn = 1, p, q
    u = 0 if n % 2 == 0 else 1
    v = 2 if n % 2 == 0 else p
    k = 1 if n % 2 == 0 else q
    n, d = n // 2, p * p - 4 * q
    while n > 0:
        u2 = mod(un * vn)
        v2 = mod(vn * vn - 2 * qn)
        q2 = mod(qn * qn)
        n2 = n // 2
        if n % 2 == 1:
            uu = half(u * v2 + u2 * v)
            vv = half(v * v2 + d * u * u2)
            u, v, k = uu, vv, k * q2
        un, vn, qn, n = u2, v2, q2, n2
    return u, v, k

def jacobi(a :int, n :int) -> int:
    if n <= 0 or not(n & 1):
        raise ValueError("jacobi: n cannot be 0 or even")
    a %= n
    t = 1
    while a:
        z = -1 if n % 8 in [3, 5] else 1
        while not(a & 1):
            a = a >> 1
            t *= z

        if a % 4 == 3 and n % 4 == 3:
            t = -t

        a, n = n % a, a

    return t if n == 1 else 0

def gcd(a : int,b :int) -> int: # euclid's algorithm
    if b == 0: return a
    return gcd(b, a%b)

if __name__ == "__main__":
    main()