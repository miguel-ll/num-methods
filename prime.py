# Numerical methods for prime numbers.

from random import randint

# Fermat primality test
def fermat_test(n):
  for _ in range(100):
    a = randint(2,n-2)
    if pow(a,n-1,n) != 1:
      return False
  return True

def milTst(d, n):
    # Pick a random number in [2..n-2]
    a = 2 + randint(1, n - 4);
    # Compute a^d % n
    x = pow(a, d, n);
    if (x == 1 or x == n - 1):
        return True;
    # Keep squaring x while one of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;

# Miller-Rabin test. It returns false if n is composite and returns true if n is probably prime. k is an input parameter that determines accuracy level. Higher value of k indicates more accuracy.
def miller_test(n, k):
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    # Iterate given number of 'k' times
    for i in range(k):
        if (milTst(d, n) == False):
            return False;
    return True;

#k = 4;
#n = 20
#if (isPrime(n,k)):
#    print(n)
#else:
#    print("no")

# Sieve of Atkin
def sieve_atkin(limit):
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    # Initialise the sieve array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
            # Main part of Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
        r += 1
    # Using sieve[]
    for a in range(5, limit+1):
        if sieve[a]:
            print(a, end=" ")

def fillPrimes(chprime, high):
    ck = [True]*(high+1)
    l = int(sqrt(high))
    for i in range(2, l+1):
        if ck[i]:
            for j in range(i*i, l+1, i):
                ck[j] = False
    for k in range(2, l+1):
        if ck[k]:
            chprime.append(k)

# print prime numbers from low to high
def segsieve(low, high):
    chprime = list()
    fillPrimes(chprime, high)
# chprimes has primes in range [2,sqrt(n)]
# we take primes from 2 to sqrt[n] because the multiples of all primes below high are marked by these
    prime = [True] * (high-low + 1)
# here prime[0] indicates whether low is prime or not similarly prime[1] indicates whether low+1 is prime or not
    for i in chprime:
        lower = (low//i)
# here lower means the first multiple of prime which is in range [low,high]
# for eg: 3's first multiple in range [28,40] is 30
        if lower <= 1:
            lower = i+i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower*i
        for j in range(lower, high+1, i):
            prime[j-low] = False
    for k in range(low, high + 1):
            if prime[k-low]:
                print(k, end=" ")

#limit = 30
#sieveatkin(limit)
