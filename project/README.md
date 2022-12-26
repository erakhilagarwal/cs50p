# Random prime number generator with given digits
## Video Demo:  https://youtu.be/HYTDE7NQvFI

## Author:
#### Akhil Agarwal
er.akhilagarwal@gmail.com
https://linkedin.com/erakhilagarwal

## Description:
This program generates a prime number with given number of digits.

A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number.

For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4.

Primes are central in number theory because of the fundamental theorem of arithmetic: every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order.

The first 25 prime numbers (all the prime numbers less than 100) are:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

No even number n greater than 2 is prime because any such number can be expressed as the product 2 × n/2. Therefore, every prime number other than 2 is an odd number, and is called an odd prime.


## Computer applications of prime numbers
Several public-key cryptography algorithms, such as RSA and the Diffie–Hellman key exchange, are based on large prime numbers (2048-bit primes are common).

RSA relies on the assumption that it is much easier (that is, more efficient) to perform the multiplication of two (large) numbers x and y than to calculate x and y (assumed coprime) if only the product xy is known.

The Diffie–Hellman key exchange relies on the fact that there are efficient algorithms for modular exponentiation a^b mod c, while the reverse operation (the discrete logarithm) is thought to be a hard problem.

Prime numbers are frequently used for hash tables. For instance the original method of Carter and Wegman for universal hashing was based on computing hash functions by choosing random linear functions modulo large prime numbers. Carter and Wegman generalized this method to k-independent hashing by using higher-degree polynomials, again modulo large primes. As well as in the hash function, prime numbers are used for the hash table size in quadratic probing based hash tables to ensure that the probe sequence covers the whole table.

Some checksum methods are based on the mathematics of prime numbers. For instance the checksums used in International Standard Book Numbers are defined by taking the rest of the number modulo 11, a prime number. Because 11 is prime this method can detect both single-digit errors and transpositions of adjacent digits. Another checksum method, Adler-32, uses arithmetic modulo 65521, the largest prime number less than 2^16. Prime numbers are also used in pseudorandom number generators including linear congruential generators and the Mersenne Twister

## Help:
project/ $ python project.py -h
>usage: project [-h] [-d [1-300]]
>
>Generates randon prime number with given digits
>
>options:
>  -h, --help            show this help message and exit
>
>  -d [1-300], --digits [1-300]
>                        Number of digits for prime >number. Default is 10 (must be in
>                        range 1..=300)
>
>Created by Akhil Agarwal (er.akhilagarwal@gmail.com)

## Examples
$ python project.py --digits 30
>516516887257706713972968092099

$python project.py
>1855398287

## How it works:
To generate a prime, all we do is pick a random number in the desired range over and over again until we find one that's prime. Nothing fancy. In fact, no one really knows a better way to find primes!

This means we run a lot of tests of the form "is this number prime?" We use the Baillie-PSW primality test to answer this question. It has been proven to always work on numbers with up to 64 bits (18 digits), and no one has ever found a composite number that it thinks is prime.

The Baillie–PSW primality test is a probabilistic primality testing algorithm that determines whether a number is composite or is a probable prime. It is named after Robert Baillie, Carl Pomerance, John Selfridge, and Samuel Wagstaff.

The Baillie–PSW test is a combination of a strong Fermat probable prime test to base 2 and a strong Lucas probable prime test. The Fermat and Lucas test each have their own list of pseudoprimes, that is, composite numbers that pass the test.

There is no known overlap between these lists of strong Fermat pseudoprimes and strong Lucas pseudoprimes, and there is even evidence that the numbers in these lists tend to be different kinds of numbers.

No composite number below 264 (approximately 1.845·1019) passes the Baillie–PSW test. Consequently, this test is a deterministic primality test on numbers below that bound. There are also no known composite numbers above that bound that pass the test, in other words, there are no known Baillie–PSW pseudoprimes. Despite this, there are conjectured to be infinitely many.

### The Test
Let n be the odd positive integer that we wish to test for primality.

Optionally, perform trial division to check if n is divisible by a small prime number less than some convenient limit.
Perform a base 2 strong probable prime test. If n is not a strong probable prime base 2, then n is composite; quit.
Find the first D in the sequence 5, −7, 9, −11, 13, −15, ... for which the Jacobi symbol (D/n) is −1. Set P = 1 and Q = (1 − D) / 4.
Perform a strong Lucas probable prime test on n using parameters D, P, and Q. If n is not a strong Lucas probable prime, then n is composite. Otherwise, n is almost certainly prime.

## References:
https://en.wikipedia.org/wiki/Prime_number
https://docs.python.org/
https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test
https://en.wikipedia.org/wiki/Jacobi_symbol
https://en.wikipedia.org/wiki/Lucas_pseudoprime#Strong_Lucas_pseudoprimes
https://en.wikipedia.org/wiki/Lucas_pseudoprime#math_1
https://en.wikipedia.org/wiki/Strong_pseudoprime
https://en.wikipedia.org/wiki/Trial_division
https://docs.python.org/3/library/math.html


